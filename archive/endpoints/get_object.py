import requests
from archive.endpoints.base_endpoint import BaseEndpoint

class GetObject(BaseEndpoint):

    def get_object(self, obj_id):
        self.response = requests.get(url=f"https://api.restful-api.dev/objects/{obj_id}")
        self.response_json = self.response.json()

    def check_object_id(self, obj_id):
        assert self.response_json["id"] == obj_id
