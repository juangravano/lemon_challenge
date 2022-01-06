from src.api.nasa_api import NasaAPI
from src.helpers.nasa_api_helper import ApiHelper


class Test:
    api = NasaAPI()
    helper = ApiHelper()

    def test_get_api(self):
        response = self.api.get_all_info()
        assert response.status_code == 200

    def test_current_date(self):
        response = self.api.get_all_info()
        self.helper.current_date_assert(response)

    def test_get_unauthorized(self):
        response = self.api.get_all_info(params={'api_key': ''})
        self.helper.unauthorized_request_assert(response)
        assert response.status_code == 403
