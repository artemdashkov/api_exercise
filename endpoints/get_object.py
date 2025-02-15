import requests

class GetObject:
    response = None
    response_json = None
    def get_object(self, obj_id):
        self.response = requests.get(f"https://api.restful-api.dev/objects/{obj_id}")
        self.response_json = self.response.json()

    def check_obj_id(self, obj_id):
        assert self.response_json["id"] == obj_id

    def check_response_is_200(self):
        assert self.response.status_code == 200
