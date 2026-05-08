import time
import json

from app.pipeline.orchestrator import PipelineOrchestrator
from app.evaluation.dataset import TEST_PROMPTS


class PipelineEvaluator:

    def __init__(self):

        self.pipeline = PipelineOrchestrator()

        self.results = []

    def evaluate(self):

        total = len(TEST_PROMPTS)

        success_count = 0

        failure_count = 0

        total_latency = 0

        repair_count = 0

        clarification_count = 0

        for test in TEST_PROMPTS:

            prompt_id = test["id"]

            prompt_type = test["type"]

            prompt = test["prompt"]

            print(f"\nRUNNING TEST #{prompt_id}")
            print(f"TYPE: {prompt_type}")
            print(f"PROMPT: {prompt}")

            start = time.time()

            try:

                result = self.pipeline.run(prompt)

                latency = round(
                    time.time() - start,
                    2
                )

                total_latency += latency

                success = True

                repair_applied = result.get(
                    "repair_applied",
                    False
                )

                if repair_applied:
                    repair_count += 1

                if (
                    result.get("status")
                    == "clarification_needed"
                ):
                    clarification_count += 1

                success_count += 1

                validation_errors = result.get(
                    "validation_errors",
                    []
                )

                self.results.append({

                    "id": prompt_id,

                    "type": prompt_type,

                    "prompt": prompt,

                    "success": success,

                    "latency": latency,

                    "repair_applied": repair_applied,

                    "validation_errors": validation_errors
                })

                print("SUCCESS")
                print(f"LATENCY: {latency}s")

            except Exception as e:

                latency = round(
                    time.time() - start,
                    2
                )

                total_latency += latency

                failure_count += 1

                self.results.append({

                    "id": prompt_id,

                    "type": prompt_type,

                    "prompt": prompt,

                    "success": False,

                    "latency": latency,

                    "error": str(e)
                })

                print("FAILED")
                print("ERROR:", e)

        average_latency = round(
            total_latency / total,
            2
        )

        success_rate = round(
            (success_count / total) * 100,
            2
        )

        summary = {

            "total_tests": total,

            "successful_tests": success_count,

            "failed_tests": failure_count,

            "success_rate": success_rate,

            "average_latency": average_latency,

            "repair_triggered": repair_count,

            "clarification_requests": clarification_count
        }

        final_report = {

            "summary": summary,

            "results": self.results
        }

        with open(
            "evaluation_report.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                final_report,
                file,
                indent=2
            )

        print("\nEVALUATION COMPLETE")
        print(json.dumps(summary, indent=2))

        return final_report


if __name__ == "__main__":

    evaluator = PipelineEvaluator()

    evaluator.evaluate()