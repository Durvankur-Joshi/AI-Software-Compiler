import time


class RetryHandler:

    def execute(
        self,
        function,
        retries=3,
        delay=2
    ):

        last_error = None

        for attempt in range(retries):

            try:

                return function()

            except Exception as e:

                last_error = e

                print(
                    f"Retry Attempt {attempt + 1} Failed:"
                )

                print(str(e))

                time.sleep(delay)

        raise last_error