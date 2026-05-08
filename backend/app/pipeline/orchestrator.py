from app.pipeline.compiler_agent import CompilerAgent
from app.pipeline.validator import SchemaValidator
from app.pipeline.repair_engine import RepairEngine
from app.runtime.sqlite_runtime import SQLiteRuntime
from app.services.supabase_service import supabase
from app.generators.backend_generator import BackendGenerator
from app.pipeline.clarification_engine import ClarificationEngine
from app.pipeline.regeneration_engine import RegenerationEngine
from app.pipeline.retry_handler import RetryHandler
from app.monitoring.metrics import MetricsTracker
from app.runtime.execution_validator import ExecutionValidator
from app.runtime.project_exporter import ProjectExporter

class PipelineOrchestrator:

    def __init__(self):

        self.compiler_agent = CompilerAgent()

        self.validator = SchemaValidator()

        self.repair_engine = RepairEngine()

        self.runtime = SQLiteRuntime()

        self.backend_generator = BackendGenerator()

        self.clarification_engine = ClarificationEngine()

        self.regeneration_engine = RegenerationEngine()

        self.retry_handler = RetryHandler()

        self.metrics = MetricsTracker()
        
        self.execution_validator = ExecutionValidator()

    def run(self, user_prompt: str):

        start_time = self.metrics.start_timer()

        clarification = self.clarification_engine.analyze(
            user_prompt
        )

        if clarification["clarification_needed"]:

            return {

                "status": "clarification_needed",

                "questions": clarification["questions"]
            }

        try:

            result = self.retry_handler.execute(
                lambda: self.compiler_agent.run(
                    user_prompt
                )
            )

        except Exception as e:

            latency = self.metrics.end_timer(
                start_time
            )

            self.metrics.record_failure(
                latency
            )

            raise e

        intent = result["intent"]

        architecture = result["architecture"]

        db_schema = result["database"]

        api_schema = result["api"]

        ui_schema = result["ui"]

        auth_schema = result["auth"]
        
        business_logic = result.get(
           "business_logic",
           {}
        )

        validation_errors = self.validator.validate(
            database_schema=db_schema,
            api_schema=api_schema,
            ui_schema=ui_schema,
            auth_schema=auth_schema,
            business_logic= business_logic,
        )

        repaired = False

        if validation_errors:

            repaired = True

            api_related_errors = [

                error

                for error in validation_errors

                if (
                    "API" in error
                    or "request field" in error
                    or "response field" in error
                )
            ]

            if api_related_errors:

                try:

                    api_schema = (
                        self.regeneration_engine
                        .regenerate_api_schema(
                            user_prompt=user_prompt,
                            database_schema=db_schema,
                            validation_errors=api_related_errors
                        )
                    )

                except Exception as e:

                    print(
                        "REGENERATION FAILED:",
                        e
                    )

                    api_schema = (
                        self.repair_engine
                        .repair_api_schema(
                            api_schema,
                            db_schema
                        )
                    )

            else:

                api_schema = (
                    self.repair_engine
                    .repair_api_schema(
                        api_schema,
                        db_schema
                    )
                )

        self.runtime.create_database(
            db_schema
        )

        try:

            supabase.table(
                "generated_apps"
            ).insert({

                "prompt": user_prompt,

                "intent": intent,

                "architecture": architecture,

                "database_schema": db_schema,

                "api_schema": api_schema,

                "ui_schema": ui_schema,

                "auth_schema": auth_schema,
                
                "business_logic": business_logic,

                "validation_errors": validation_errors,

            }).execute()

        except Exception as e:

            print(
                "SUPABASE ERROR:",
                e
            )

        result["api"] = api_schema

        self.backend_generator.generate(
            result
        )
        
        execution_report = (
           self.execution_validator.validate()
        )

        latency = self.metrics.end_timer(
            start_time
        )

        self.metrics.record_success(
            latency
        )

        return {

          "intent": intent,

          "architecture": architecture,

          "database": db_schema,

          "api": api_schema,

          "ui": ui_schema,

          "auth": auth_schema,

          "business_logic": business_logic,

          "validation_errors": validation_errors,

          "repair_applied": repaired,

          "metrics": self.metrics.get_metrics(),
          
          "execution_report": execution_report,
}