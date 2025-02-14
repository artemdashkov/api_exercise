import pytest
import requests
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject


@pytest.fixture(name="obj_id")
def create_object():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

    new_object_endpoint = CreateObject()
    new_object_endpoint.new_object(payload)
    yield new_object_endpoint.response_json["id"]
    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_object(new_object_endpoint.response_json["id"])
