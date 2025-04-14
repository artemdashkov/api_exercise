import requests
from endpoints.base_endpoint import BaseEndpoint

class DeleteObject(BaseEndpoint):

    def delete_object(self, obj):
        self.response = requests.delete(url=f"https://api.restful-api.dev/objects/{obj}")
        self.response_json = self.response.json()
