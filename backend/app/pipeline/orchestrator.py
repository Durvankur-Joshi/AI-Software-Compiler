from app.pipeline.compiler_agent import CompilerAgent

        ui_schema = result["ui"]

        auth_schema = result["auth"]

        validation_errors = self.validator.validate(
            database_schema=db_schema,
            api_schema=api_schema,
            ui_schema=ui_schema,
            auth_schema=auth_schema
        )

        repaired = False

        if validation_errors:

            repaired = True

            api_schema = self.repair_engine.repair_api_schema(
                api_schema,
                db_schema
            )

        self.runtime.create_database(db_schema)

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

                "validation_errors": validation_errors,

            }).execute()

        except Exception as e:

            print("SUPABASE ERROR:", e)

        return {

            "intent": intent,

            "architecture": architecture,

            "database": db_schema,

            "api": api_schema,

            "ui": ui_schema,

            "auth": auth_schema,

            "validation_errors": validation_errors,

            "repair_applied": repaired
        }