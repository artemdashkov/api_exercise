import requests
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject
from endpoints.create_endpoint import CreateObject

payload = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}

def test_create_object():
    create_object_endpoint = CreateObject()
    create_object_endpoint.crete_object(payload)
    create_object_endpoint.check_status_is_200()

def test_get_object(obj_id):
    get_object_edpoints = GetObject()
    get_object_edpoints.get_object(obj_id)
    get_object_edpoints.check_status_is_200()
    get_object_edpoints.check_object_id(obj_id)

def test_update_object(obj_id):
    update_object_endpoint = UpdateObject()
    update_object_endpoint.update_object(obj_id)
    update_object_endpoint.check_status_is_200()
    update_object_endpoint.check_year()

def test_delete_object(obj_id):
    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_object(obj_id)
    delete_object_endpoint.check_status_is_200()

    get_object_edpoints = GetObject()
    get_object_edpoints.get_object(obj_id)
    get_object_edpoints.check_status_is_404()


