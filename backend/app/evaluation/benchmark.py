import time

from app.pipeline.orchestrator import PipelineOrchestrator

from app.evaluation.prompts import (
    REAL_WORLD_PROMPTS,
    EDGE_CASE_PROMPTS
)


pipeline = PipelineOrchestrator()


def run_benchmark():

    prompts = (
        REAL_WORLD_PROMPTS
        + EDGE_CASE_PROMPTS
    )

    results = []

    success_count = 0

    total_latency = 0

    for prompt in prompts:

        print("\n====================")
        print("PROMPT:")
        print(prompt)

        start = time.time()

        try:

            result = pipeline.run(prompt)

            latency = (
                time.time() - start
            )

            total_latency += latency

            validation_errors = result.get(
                "validation_errors",
                []
            )

            repaired = result.get(
                "repair_applied",
                False
            )

            success = (
                len(validation_errors) == 0
            )

            if success:

                success_count += 1

            benchmark_result = {

                "prompt": prompt,

                "success": success,

                "latency": latency,

                "repair_applied": repaired,

                "validation_errors": validation_errors
            }

            results.append(
                benchmark_result
            )

            print("SUCCESS")
            print(f"Latency: {latency:.2f}s")
            print(f"Repair Applied: {repaired}")
            print(
                f"Validation Errors: {validation_errors}"
            )

        except Exception as e:

            latency = (
                time.time() - start
            )

            results.append({

                "prompt": prompt,

                "success": False,

                "latency": latency,

                "error": str(e)
            })

            print("FAILED")
            print(str(e))

    average_latency = (
        total_latency / len(prompts)
    )

    print("\n====================")
    print("FINAL METRICS")
    print("====================")

    print(
        f"Total Prompts: {len(prompts)}"
    )

    print(
        f"Successful: {success_count}"
    )

    print(
        f"Success Rate: {(success_count / len(prompts)) * 100:.2f}%"
    )

    print(
        f"Average Latency: {average_latency:.2f}s"
    )


if __name__ == "__main__":

    run_benchmark()