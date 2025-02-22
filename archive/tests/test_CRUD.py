import pytest
from archive.endpoints.create_object import CreateObject
from archive.endpoints.get_object import GetObject
from archive.endpoints.update_object import UpdateObject
from archive.endpoints.delete_object import DeleteObject

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
    create_object_endpoint = CreateObject()
    create_object_endpoint.create_object(payload)
    create_object_endpoint.check_response_is_200()

@pytest.mark.test_02
def test_get_object(obj_id):
    get_object_endpoint = GetObject()
    get_object_endpoint.get_object(obj_id=obj_id)
    get_object_endpoint.check_response_is_200()
    get_object_endpoint.check_obj_id(obj_id=obj_id)

@pytest.mark.test_03
def test_update_object(obj_id):
    update_object_endpoint = UpdateObject()
    update_object_endpoint.update_object(obj_id=obj_id)
    update_object_endpoint.check_response_is_200()
    update_object_endpoint.check_id(obj_id)
    update_object_endpoint.check_data_without_id()

@pytest.mark.test_04
def test_delete(obj_id):
    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_object(obj_id=obj_id)
    delete_object_endpoint.check_response_is_200()
