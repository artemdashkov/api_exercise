import requests
from base_endpoint import BaseEndpoint

class UpdateObject(BaseEndpoint):

    def update_object(self, obj_id, payload):
        self.response = requests.put(url=f"https://api.restful-api.dev/objects/{obj_id}",
                                json=payload)
        self.response_json = self.response.json()

    def check_year(self, payload):
        assert payload["data"]["year"] == self.response_json["data"]["year"]

