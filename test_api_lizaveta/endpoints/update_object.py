import allure
import requests

from endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):

    @allure.step('Update an object with PUT')
    def update_object(self, object_id, payload):
        self.response = requests.put(
            f'{self.url}/{object_id}',
            json=payload,
            headers=self.headers
        )
        self.json = self.response.json()
