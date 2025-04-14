import requests
from endpoints.create_endpoint import CreateObject
from endpoints.get_endpoint import GetObject
from endpoints.update_endpoint import UpdateObject
from endpoints.delete_endpoint import DeleteObject


def test_create_object():
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
    create_object_endpoint.create_object(payload)
    create_object_endpoint.check_name(payload["name"])
    create_object_endpoint.status_is_200()
    create_object_endpoint.delete_object()
    create_object_endpoint.status_is_200()

def test_get_object(obj_id):
    get_object_endpoint = GetObject()
    get_object_endpoint.get_endpoint(obj_id)
    get_object_endpoint.check_object_id(obj_id)
    get_object_endpoint.status_is_200()

def test_update_object(obj_id):
    update_object = UpdateObject()
    update_object.update_put_endpoint(obj_id)
    update_object.status_is_200()
    update_object.check_object_id(obj_id)
    update_object.check_name()

def test_delete_object(obj_id):
    delete_object = DeleteObject()
    delete_object.delete_object(obj_id)
    delete_object.status_is_200()

    get_object_endpoint = GetObject()
    get_object_endpoint.get_endpoint(obj_id)
    get_object_endpoint.status_is_404()



