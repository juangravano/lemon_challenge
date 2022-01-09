from src.api.nasa_api import NasaAPI
from src.helpers.nasa_api_helper import ApiHelper


class TestApiAPOD:
    api = NasaAPI()
    helper = ApiHelper()

    def test_current_date(self):
        """
        TEST: se envía una petición con los parámetros por defecto, debe devolver la publicación de la fecha actual.
        """
        response = self.api.get_apod()
        self.helper.assert_current_date(response)
        assert response.status_code == 200

    def test_specific_date(self):
        """
        TEST: se envía una petición con una fecha especifica, debe devolver la publicación de dicha fecha.
        """
        response = self.api.get_apod(params={'api_key': self.api.api_key,
                                             'date': '2021-12-31'})
        assert response.status_code == 200
        assert response.json()['date'] == '2021-12-31'

    def test_range_date(self):
        """
        TEST: se envía una petición con un rango de fechas, debe devolver las publicaciones de dicho rango.
        Se valida que se devuelva una lista de publicaciones del mismo tamaño que días transcurridos.
        """
        response = self.api.get_apod(params={'api_key': self.api.api_key,
                                             'start_date': '2021-12-31',
                                             'end_date': '2022-01-05'})
        assert response.status_code == 200
        assert (len(response.json())) == 6

    def test_get_unauthorized(self):
        """
        TEST: se envía una petición sin ApiKey, la misma debe ser rechazada.
        """
        response = self.api.get_apod(params={'api_key': ''})
        self.helper.assert_unauthorized_request(response)
        assert response.status_code == 403

    def test_thumbs_parameter_is_true(self):
        """
        TEST: se envía una petición con el parámetros thumbs = True, debe devolver la publicación de la fecha actual.
        """
        response = self.api.get_apod(params={'api_key': self.api.api_key,
                                             'thumbs': True})
        assert response.status_code == 200

    def test_count_parameter_is_random(self):
        """
        TEST: se envía una petición con el parámetro count con un valor aleatorio entre 1 y 10.
        Se valida que se devuelva una lista de publicaciones del mismo tamaño que el parámetro count
        """
        response = self.api.get_apod(params={'api_key': self.api.api_key,
                                             'count': self.helper.count})
        self.helper.assert_count_parameter_is_random(response)
        assert response.status_code == 200

    def test_count_parameter_with_date(self):
        """
        TEST: se envía una petición con los parámetros por count, start_date y end_date,
        No es una combinación de parámetros válida.
        """
        response = self.api.get_apod(params={'api_key': self.api.api_key,
                                             'start_date': '2021-12-31',
                                             'end_date': '2022-01-05',
                                             'count': self.helper.count})
        self.helper.assert_apod_bad_request_400(response)
