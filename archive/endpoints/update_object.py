import requests
from archive.endpoints.base_endpoint import Endpoint

class UpdateObject(Endpoint):

    def update_object(self, payload, obj_id):
        self.response = requests.put(
            url=f"https://api.restful-api.dev/objects/{obj_id}",
            json=payload
        )
        self.response_json = self.response.json()

    def check_year(self, year):
        assert self.response_json["data"]["year"] == year
