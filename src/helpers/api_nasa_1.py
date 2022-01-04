from src.api.api_client import ApiClient

class ApiNasa:
    api_url = 'https://api.nasa.gov/'
    api_key = 'HAjFqcLlRWvvQWR9DaxufozPTcbbxMidB5qY6uDO'
    api_client = ApiClient(api_url)

    def get_all_info(self, params=None):
        if params is None:
            params = {'api_key': self.api_key}
        response = self.api_client.get(path='planetary/apod', params=params, headers={})
        return response
