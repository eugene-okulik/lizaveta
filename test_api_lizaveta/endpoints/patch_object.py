import allure
import requests

from endpoints.endpoint import Endpoint


class PatchObject(Endpoint):

    @allure.step('Update an object with PATCH')
    def patch_object(self, object_id, payload):
        self.response = requests.patch(
            f'{self.url}/{object_id}',
            json=payload,
            headers=self.headers
        )
        self.json = self.response.json()
