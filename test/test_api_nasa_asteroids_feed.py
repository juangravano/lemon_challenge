from src.api.nasa_api import NasaAPI
from src.helpers.nasa_api_helper import ApiHelper


class TestApiAsteroids:
    api = NasaAPI()
    helper = ApiHelper()

    def test_get_end_date_default(self):
        """
        Se envía una petición con start_date indicada y end_date por defecto.
        Se debe recibir una lista de publicaciones con las publicaciones de siete dias posteriores a la fecha de start_date
        """
        response = self.api.get_asteroid_feed()
        assert len(response.json()) >= 1
        assert response.status_code == 200

    def test_get_without_start_date(self):
        """
        Se envía una petición con start_date por defecto
        Se debe recibir la lista historica de publicaciones
        """
        response = self.api.get_asteroid_feed(params={'api_key': self.api.api_key})
        assert len(response.json()) >= 1
        assert response.status_code == 200

    def test_get_without_start_date_and_end_date(self):
        """
        Se envía una petición con start_date y end_date
        Se debe recibir una lista con las publicaciones entre esos días
        """
        response = self.api.get_asteroid_feed(params={'start_date': '2021-01-10',
                                                      'end_date': '2021-01-11',
                                                      'api_key': self.api.api_key})
        assert len(response.json()) >= 1
        assert response.status_code == 200

    def test_get_without_api_key(self):
        """
        TEST: se envía una petición sin ApiKey, la misma debe ser rechazada.
        """
        response = self.api.get_asteroid_feed(params={'api_key': ''})
        self.helper.assert_unauthorized_request(response)
