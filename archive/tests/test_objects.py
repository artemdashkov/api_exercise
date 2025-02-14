from archive.endpoints.create_object import CreateObject
from archive.endpoints.get_object import GetObject
from archive.endpoints.update_object import UpdateObject
from archive.endpoints.delete_object import DeleteObject

payload = {
           "name": "Apple MacBook Pro 20",
           "data": {
              "year": 2020,
              "price": 1849.99,
              "CPU model": "Intel Core i9",
              "Hard disk size": "1 TB"
           }
        }

def test_create_object():
    new_object_endpoint = CreateObject()
    payload = {
       "name": "Apple MacBook Pro 16",
       "data": {
          "year": 2019,
          "price": 1849.99,
          "CPU model": "Intel Core i9",
          "Hard disk size": "1 TB"
       }
    }
    new_object_endpoint.new_object(payload=payload)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_name(payload['name'])

def test_get_object(obj_id):
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_by_id(obj_id)
    get_obj_endpoint.check_response_is_200()
    get_obj_endpoint.check_response_id(obj_id)

def test_update_object(obj_id):
    update_object_endpoint = UpdateObject()
    update_object_endpoint.update_object(payload=payload, obj_id=obj_id)
    update_object_endpoint.check_response_is_200()
    update_object_endpoint.check_year(payload["data"]["year"])


def test_delete_object(obj_id):
    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_object(obj_id)
    delete_object_endpoint.check_response_is_200()
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_by_id(obj_id)
    get_obj_endpoint.check_response_is_404()