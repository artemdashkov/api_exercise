import pytest
import requests

from endpoints.create_endpoint import CreateObject
from endpoints.delete_object import DeleteObject

@pytest.fixture(name="obj_id")
def create_and_delete():
    create_object_endpoint = CreateObject()
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    create_object_endpoint.crete_object(payload)
    object_id = create_object_endpoint.response_json["id"]
    yield object_id
    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_object(object_id)
