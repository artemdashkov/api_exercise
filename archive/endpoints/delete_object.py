import requests
from archive.endpoints.base_endpoints import BaseEndpoint

class DeleteObject(BaseEndpoint):

    def delete_object(self, obj_id):
        self.response = requests.delete(f"https://api.restful-api.dev/objects/{obj_id}")
        self.response_json = self.response.json()
