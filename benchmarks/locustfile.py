from locust import HttpUser, between, task


class ApiUser(HttpUser):
    wait_time = between(0.0, 0.05)

    @task(1)
    def health(self):
        self.client.get("/health")

    @task(6)
    def compute_light(self):
        self.client.get("/compute/1000", name="/compute/[iterations] light")

    @task(3)
    def compute_heavy(self):
        self.client.get("/compute/50000", name="/compute/[iterations] heavy")
