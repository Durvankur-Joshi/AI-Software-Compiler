import time


class MetricsTracker:

    def __init__(self):

        self.total_requests = 0

        self.successful_requests = 0

        self.failed_requests = 0

        self.total_latency = 0

    def start_timer(self):

        return time.time()

    def end_timer(self, start_time):

        return round(
            time.time() - start_time,
            2
        )

    def record_success(
        self,
        latency
    ):

        self.total_requests += 1

        self.successful_requests += 1

        self.total_latency += latency

    def record_failure(
        self,
        latency
    ):

        self.total_requests += 1

        self.failed_requests += 1

        self.total_latency += latency

    def get_metrics(self):

        average_latency = 0

        if self.total_requests > 0:

            average_latency = (
                self.total_latency
                / self.total_requests
            )

        success_rate = 0

        if self.total_requests > 0:

            success_rate = (
                self.successful_requests
                / self.total_requests
            ) * 100

        return {

            "total_requests":
                self.total_requests,

            "successful_requests":
                self.successful_requests,

            "failed_requests":
                self.failed_requests,

            "success_rate":
                round(success_rate, 2),

            "average_latency":
                round(average_latency, 2)
        }