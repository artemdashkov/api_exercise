import requests
from endpoints.base_endpoint import BaseEndpoint

class CreateObject(BaseEndpoint):
    object_id = None

    def create_object(self, payload):
        self.response = requests.post(url="https://api.restful-api.dev/objects", json=payload)
        self.response_json = self.response.json()
        self.object_id = self.response_json["id"]

    def check_name(self, name):
        assert self.response_json["name"] == name

    def delete_object(self):
        self.response = requests.delete(url=f"https://api.restful-api.dev/objects/{self.object_id}")
        self.response_json = self.response.json()