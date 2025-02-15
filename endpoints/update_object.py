import requests
from faker import Faker
from endpoints.base_endpoints import BaseEndpoint

class UpdateObject(BaseEndpoint):
    payload = None

    def update_object(self, obj_id):
        fake = Faker()
        name = fake.name()
        self.payload = {
            "name": name,
            "data": {
                "year": 2019,
                "price": 2049.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB",
                "color": "silver"
            }
        }
        self.response = requests.put(f"https://api.restful-api.dev/objects/{obj_id}",
                                     json=self.payload)
        self.response_json = self.response.json()

    def check_id(self, obj_id):
        assert self.response_json["id"] == obj_id

    def check_data_without_id(self):
        del self.response_json["id"]
        del self.response_json["updatedAt"]
        assert self.response_json == self.payload
