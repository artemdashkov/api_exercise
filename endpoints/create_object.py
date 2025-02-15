import requests

class CreateObject:
    response = None
    def create_object(self, payload):
        self.response = requests.post("https://api.restful-api.dev/objects",
                                 json=payload)
        self.response_json = self.response.json()

    def check_response_is_200(self):
        assert self.response.status_code == 200