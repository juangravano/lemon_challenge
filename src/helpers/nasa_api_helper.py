from src.logger import Log
from datetime import date

class ApiHelper:

    def assert_current_date(self, response):
        current_date = str(date.today())
        assert response.json()['date'] == current_date, f'The current date is {current_date}'

    def assert_unauthorized_request(self, response):
        message = 'No api_key was supplied. Get one at https://api.nasa.gov:443'
        code = 'API_KEY_MISSING'
        assert response.json()['error']['message'] == message, f"The message is {response.json()['error']['message']}"
        assert response.json()['error']['code'] == code, f"The code is {response.json()['error']['code']}"
        assert response.status_code == 403

    def assert_count_parameter_is_random(self, response):
        import random
        count = random.randint(1, 10)
        assert len(response.json()) == self.count
        
    def assert_apod_bad_request_400(self, response):
        assert response.status_code == 400
        assert response.json() == {'code': 400, 'msg': "Bad Request: invalid field combination passed. Allowed request fields for apod method are 'concept_tags', 'date', 'hd', 'count', 'start_date', 'end_date', 'thumbs'", 'service_version': 'v1'}