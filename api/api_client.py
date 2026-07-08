import requests


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        response = requests.get(
            self.base_url + endpoint
        )
        return response

    def post(self, endpoint, payload):
        response = requests.post(
            self.base_url + endpoint,
            json=payload
        )
        return response