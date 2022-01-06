import requests
from src.logger import Log


class ApiClient:
    log = Log()
    log = log.get_logger(__name__)

    def __init__(self, url):
        self.url = url

    def get(self, path='', params=None, headers=None):
        """
        Método para realizar petición GET
        :param path: Opcional - Endpoint a invocar
        :param params: Opcional - Query params a enviar al servicio
        :param headers: Opcional - Header a enviar al servicio
        :return: Respuesta del servicio
        """
        request_url = self.url + path
        self.log.info(f'Get to {request_url}')
        response = requests.get(url=request_url, params=params, headers=headers)
        self.log.info(f'status code: {response.status_code}')
        self.log.info(f'response: {response.json()}')
        return response

    def post(self, path='', body='', params=None, headers=None):
        """
        Método para realizar petición POST
        :param path: Opcional - Endpoint a invocar
        :param body: Payload a enviar al servicio
        :param params: Opcional - Query params a enviar al servicio
        :param headers: Opcional - Header a enviar al servicio
        :return: Respuesta del servicio
        """
        request_url = self.url + path
        self.log.info(f'Post to {request_url}')
        response = requests.post(url=request_url, data=body, params=params, headers=headers)
        self.log.info(f'status code: {response.status_code}')
        self.log.info(f'response: {response.json()}')
        return response

    def put(self, path='', body='', params=None, headers=None):
        """
        Método para realizar petición PUT
        :param path: Opcional - Endpoint a invocar
        :param body: Payload a enviar al servicio
        :param params: Opcional - Query params a enviar al servicio
        :param headers: Opcional - Header a enviar al servicio
        :return: Respuesta del servicio
        """
        request_url = self.url + path
        self.log.info(f'Put to {request_url}')
        response = requests.put(url=request_url, data=body, params=params, headers=headers)
        self.log.info(f'status code: {response.status_code}')
        self.log.info(f'response: {response.json()}')
        return response

    def delete(self, path='', params=None, headers=None):
        """
        Método para realizar petición DELETE
        :param path: Opcional - Endpoint a invocar
        :param params: Opcional - Query params a enviar al servicio
        :param headers: Opcional - Header a enviar al servicio
        :return: Respuesta del servicio
        """
        request_url = self.url + path
        self.log.info(f'Delete to {request_url}')
        response = requests.get(url=request_url, params=params, headers=headers)
        self.log.info(f'status code: {response.status_code}')
        self.log.info(f'response: {response.json()}')
        return response
