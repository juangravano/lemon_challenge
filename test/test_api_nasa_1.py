from src.helpers.api_nasa_1 import ApiNasa
from src.logger import Log


class Test:
    api = ApiNasa()

    def test_get_api(self):
        response = self.api.get_all_info()
        assert response.status_code == 200

    def test_get_unauthorized(self):
        response = self.api.get_all_info(params={'api_key': ''})
        assert response.status_code == 403
