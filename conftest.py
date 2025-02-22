import pytest
import requests

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

    response = requests.post(url="https://api.restful-api.dev/objects",
                             json=payload)
    response_json = response.json()
    id = response_json["id"]
    yield id
    requests.delete(url=f"https://api.restful-api.dev/objects/{id}")
