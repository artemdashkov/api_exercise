import pytest
import requests

from endpoints.create_endpoint import CreateObject

@pytest.fixture(name="obj_id")
def create_and_delete():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

    create_object_endpoint = CreateObject()
    create_object_endpoint.crete_object(payload)
    object_id = create_object_endpoint.response_json["id"]
    yield object_id
    requests.delete(url=f"https://api.restful-api.dev/objects/{object_id}")
