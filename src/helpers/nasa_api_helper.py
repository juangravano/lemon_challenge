from src.logger import Log
from datetime import date


class ApiHelper:

    def current_date_assert(self, response):
        current_date = str(date.today())
        assert response.json()['date'] == current_date, f'The current date is {current_date}'

    def unauthorized_request_assert(self, response):
        message = 'No api_key was supplied. Get one at https://api.nasa.gov:443'
        code = 'API_KEY_MISSING'
        assert response.json()['error']['message'] == message, f"The message is {response.json()['error']['message']}"
        assert response.json()['error']['code'] == code, f"The code is {response.json()['error']['code']}"
        assert response.status_code == 403
