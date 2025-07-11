import requests
import pytest

info_for_add_object = {
       "name": "Apple MacBook Pro 16",
       "data": {
          "year": 2019,
          "price": 1849.99,
          "CPU model": "Intel Core i9",
          "Hard disk size": "1 TB"
           }
        }

info_for_add_object_v2 = {
       "name": "Samsung",
       "data": {
          "year": 2020
           }
        }

@pytest.mark.create_object
def test_create_object():

    response = requests.post(url="https://api.restful-api.dev/objects",
                                  json=info_for_add_object)
    status_code = response.status_code
    assert status_code  == 200, \
        f"Status code don't 200, got code is: {status_code }"

@pytest.mark.get_object
def test_get_object():
    response = requests.post(url="https://api.restful-api.dev/objects",
                             json=info_for_add_object,)
    response_json = response.json()
    status_code = response.status_code
    id = response_json["id"]
    response_get_object = requests.get(url=f"https://api.restful-api.dev/objects/{id}")
    response_get_object_json = response_get_object.json()
    assert response_get_object.status_code == 200,  \
        f"Status code don't 200, got code is: {status_code }"
    assert response_get_object_json["id"] == id

@pytest.mark.update_object_patch
def test_update_object():
    response = requests.post(url="https://api.restful-api.dev/objects",
                             json=info_for_add_object)
    status_code = response.status_code
    response_json = response.json()
    id = response_json["id"]
    assert status_code == 200, \
        f"Status code don't 200, got code is: {status_code}"
    response_patch = requests.patch(url=f"https://api.restful-api.dev/objects/{id}",
                             json=info_for_add_object_v2)
    response_patch_json = response_patch.json()
    print(response_patch_json)
    assert response_patch_json["name"] == info_for_add_object_v2["name"]
    assert response_patch_json["data"]["year"] == info_for_add_object_v2["data"]["year"]


@pytest.mark.delete_object
def test_delete_object():
    response = requests.post(url="https://api.restful-api.dev/objects", json=info_for_add_object)
    response_json = response.json()
    id_object = response_json['id']
    response = requests.delete(url=f"https://api.restful-api.dev/objects/{id_object}")
    assert response.status_code == 200, f"Expected status code isn't 200, current code {response.status_code}"
    response_get = requests.get(url=f"https://api.restful-api.dev/objects/{id_object}")
    assert response_get.status_code == 404, f"Expected status code isn't 404, current code {response.status_code}"

