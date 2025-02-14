import requests

class DeleteObject:
    response = None
    response_json = None

    def delete_object(self, obj_id):
        self.response = requests.delete(f"https://api.restful-api.dev/objects/{obj_id}")
        self.response_json = self.response.json()

    def check_response_is_200(self):
        assert self.response.status_code == 200