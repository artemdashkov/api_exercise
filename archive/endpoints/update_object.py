import requests
from archive.endpoints.base_endpoint import BaseEndpoint

class UpdateObject(BaseEndpoint):
    payload = {
               "name": "Apple MacBook Pro 16",
               "data": {
                  "year": 2020,
                  "price": 2049.99,
                  "CPU model": "Intel Core i9",
                  "Hard disk size": "1 TB",
                  "color": "silver"
                   }
                }

    def update_object(self, obj_id):
        self.response = requests.put(url=f"https://api.restful-api.dev/objects/{obj_id}",
                                json=self.payload)
        self.response_json = self.response.json()

    def check_year(self):
        assert self.payload["data"]["year"] == self.response_json["data"]["year"]

