import allure
import requests

from endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    object_id = None

    @allure.step('Create new object')
    def create_new_object(self, payload):
        self.response = requests.post(
            self.url,
            json=payload,
            headers=self.headers
        )
        self.json = self.response.json()
        self.object_id = self.json['id']
