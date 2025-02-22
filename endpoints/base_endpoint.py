import requests

class BaseEndpoint:
    response = None
    response_json = None

    def check_status_is_200(self):
        assert self.response.status_code == 200