import requests
from endpoints.base_endpoint import BaseEndpoint

class UpdateObject(BaseEndpoint):
    payload_new = {
        "name": "Lenovo",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    def update_put_endpoint(self, id):
        self.response = requests.patch(f"https://api.restful-api.dev/objects/{id}",
                                       json=self.payload_new)
        self.response_json = self.response.json()

    def check_object_id(self, id):
        assert self.response_json["id"] == id

    def check_name(self):
        assert self.response_json["name"] == self.payload_new["name"]
