import requests
from archive.endpoints.base_endpoints import BaseEndpoint

class CreateObject(BaseEndpoint):

    def create_object(self, payload):
        self.response = requests.post("https://api.restful-api.dev/objects",
                                 json=payload)
        self.response_json = self.response.json()
