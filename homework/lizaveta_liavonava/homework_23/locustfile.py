from locust import task, HttpUser, between
import random


class ObjectUser(HttpUser):
    wait_time = between(1, 4)

    def on_start(self):
        response = self.client.post(
            '/object',
            json={"data": {"color": "black", "size": "small"}, "name": "super new object"},
        )
        self.object_id = response.json()["id"]

    def on_stop(self):
        self.client.delete(
            f'/object/{self.object_id}',
        )

    @task(1)
    def get_all_objects(self):
        self.client.get(
            '/object'
        )

    @task(3)
    def get_one_object(self):
        self.client.get(
            f'/object/{random.randint(1, 10)}',
            name='/object/[random_id]'
        )

    @task
    def get_new_object(self):
        self.client.get(
            f'/object/{self.object_id}'
        )

    @task
    def put_new_object(self):
        self.client.put(
            f'/object/{self.object_id}',
            json={"data": {"color": "white", "size": "huge"}, "name": "super new object 2"},
        )
