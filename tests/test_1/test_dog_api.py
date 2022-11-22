import pytest
import requests
from jsonschema import validate
from data_for_test_1 import BASE_URL_1, ENDPOINTS_1, breeds_all, breeds_with_sub_breed_only
from schemas_1 import SCHEMA_1, SCHEMA_2, SCHEMA_3


@pytest.mark.smoke
@pytest.mark.parametrize("endpoint", ENDPOINTS_1.values(), ids=ENDPOINTS_1.keys())
def test_endpoints_status_dog_api(endpoint):
    response = requests.get(endpoint)
    data = response.json()
    assert response.status_code == 200
    assert len(data["message"]) != 0
    assert "success" in data["status"]


@pytest.mark.smoke
@pytest.mark.parametrize("endpoint, schema", [
    (ENDPOINTS_1["List all breeds"], SCHEMA_1),
    (ENDPOINTS_1["Display single random image from all dogs collection"], SCHEMA_3),
    (ENDPOINTS_1["By breed"], SCHEMA_2),
    (ENDPOINTS_1["List all sub-breeds"], SCHEMA_2),
    (ENDPOINTS_1["Multiple images from a breed collection"], SCHEMA_2),
    (ENDPOINTS_1["Breeds list"], SCHEMA_3)
], ids=ENDPOINTS_1.keys())
def test_validate_endpoints_dog_api(endpoint, schema):
    response = requests.get(endpoint)
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)


@pytest.mark.regress
@pytest.mark.parametrize("breed", breeds_all)
def test_breeds_list(breed):
    response = requests.get(f"{BASE_URL_1}/breed/{breed}/images/random")
    data = response.json()
    assert response.status_code == 200
    assert len(data["message"]) != 0
    assert (".jpg" in data["message"]) and (breed in data["message"])


@pytest.mark.regress
@pytest.mark.parametrize("num", [1, 15, 34])
@pytest.mark.parametrize("breed", breeds_all)
def test_return_multiple_random_img_from_a_breed(num, breed):
    response = requests.get(f"{BASE_URL_1}/breed/{breed}/images/random/{num}")
    data = response.json()
    assert response.status_code == 200
    assert len(data["message"]) == num
    for img in data["message"]:
        assert (".jpg" in img) and (f"{breed}" in img)


@pytest.mark.regress
@pytest.mark.parametrize("breed", breeds_with_sub_breed_only)
def test_list_all_sub_breeds(breed):
    response = requests.get(f"{BASE_URL_1}/breed/{breed}/list")
    data = response.json()
    assert response.status_code == 200
    assert len(data["message"]) > 0
    assert "success" in data["status"]
