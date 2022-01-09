from src.api.api_client import ApiClient
from src.logger import Log


class NasaAPI:
    log = Log()
    log = log.get_logger(__name__)
    api_url = 'https://api.nasa.gov/'
    api_key = 'HAjFqcLlRWvvQWR9DaxufozPTcbbxMidB5qY6uDO'
    api_client = ApiClient(api_url)
    endpoint_apod = 'planetary/apod'
    endpoint_asteroid_feed = 'neo/rest/v1/feed'

    def get_apod(self, params=None):
        if params is None:
            params = {'api_key': self.api_key}
        response = self.api_client.get(path=self.endpoint_apod, params=params, headers={})
        return response

    def get_asteroid_feed(self, params=None):
        if params is None:
            params = {'start_date': '2021-01-10',
                      'api_key': self.api_key}
        response = self.api_client.get(path=self.endpoint_asteroid_feed, params=params, headers={})
        return response