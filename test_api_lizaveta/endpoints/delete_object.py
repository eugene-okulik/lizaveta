import allure
import requests

from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Delete an object')
    def delete_object(self, object_id):
        self.response = requests.delete(f'{self.url}/{object_id}')

    @allure.step('Check that object is deleted')
    def check_object_is_deleted(self, object_id):
        response = requests.get(f'{self.url}/{object_id}')
        assert response.status_code == 404
