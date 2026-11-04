import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Check that response name is correct')
    def check_response_name_is_correct(self, name):
        assert self.response.json()['name'] == name

    @allure.step('Check that response data is correct')
    def check_response_data_is_correct(self, data):
        assert self.response.json()['data'] == data
