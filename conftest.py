import requests
import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject

@pytest.fixture(name="obj_id")
def create_delete_obj():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

    create_obj_endpoints = CreateObject()
    create_obj_endpoints.create_object(payload)
    id = create_obj_endpoints.response_json["id"]
    yield id
    delete_obj_endpoints = DeleteObject()
    delete_obj_endpoints.delete_object(id)
