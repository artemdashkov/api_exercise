import requests
from archive.endpoints.base_endpoint import Endpoint

class DeleteObject(Endpoint):
    def delete_object(self, obj_id):
        self.response = requests.delete(url=f"https://api.restful-api.dev/objects/{obj_id}")
        self.response_json = self.response.json()

    def response_is_404(self):
        assert self.response.status_code == 404
