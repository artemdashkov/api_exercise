import requests
import pytest
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject

payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

@pytest.mark.test_01
def test_create():
    response = requests.post("https://api.restful-api.dev/objects", json=payload)
    response_json = response.json()
    assert response.status_code == 200
    odj_name = response_json["name"]
    assert payload["name"] == odj_name

@pytest.mark.test_02
def test_get_object(obj_id):
    response = requests.get(f"https://api.restful-api.dev/objects/{obj_id}")
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["id"] == obj_id

@pytest.mark.test_03
def test_update_object(obj_id):
    update_object_endpoint = UpdateObject()
    update_object_endpoint.update_object(obj_id=obj_id)
    update_object_endpoint.check_response_is_200()
    update_object_endpoint.check_id(obj_id)
    update_object_endpoint.check_data_without_id()


def test_delete(obj_id):
    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_object(obj_id=obj_id)
    delete_object_endpoint.check_response_is_200()
