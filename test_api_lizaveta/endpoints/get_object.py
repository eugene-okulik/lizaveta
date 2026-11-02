import allure
import requests

from endpoints.endpoint import Endpoint


class GetObject(Endpoint):

    @allure.step('Get an object')
    def get_object(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}')
        self.json = self.response.json()

    @allure.step('Check that response id is correct')
    def check_response_id_is_correct(self, object_id):
        assert self.json['id'] == object_id
