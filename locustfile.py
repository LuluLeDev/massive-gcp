from locust import HttpUser, task, between
import random

class TinyInstaUser(HttpUser):
    wait_time = between(0.5, 1.5)

    @task
    def get_timeline(self):
        user_id = f"user{random.randint(1, 1000)}"
        self.client.get(f"/api/timeline?user={user_id}&limit=20", name="/api/timeline")