import pytest
import requests
from jsonschema import validate
from random import choice, randint
from data_for_test_2 import ENDPOINTS_2, BASE_URL_2, brewery_id, brewery_types
from schemas_2 import SCHEMA_1, SCHEMA_2


@pytest.mark.smoke
@pytest.mark.parametrize("endpoint", ENDPOINTS_2.values(), ids=ENDPOINTS_2.keys())
def test_endpoints_status_brewery_api(endpoint):
    response = requests.get(endpoint)
    data = response.json()
    assert response.status_code == 200
    assert len(data) != 0


@pytest.mark.smoke
@pytest.mark.parametrize("endpoint, schema", [
    (ENDPOINTS_2["Single Brewery"], SCHEMA_2),
    (ENDPOINTS_2["List Breweries"], SCHEMA_1),
    (ENDPOINTS_2["Random Brewery"], SCHEMA_1)
], ids=ENDPOINTS_2.keys())
def test_validate_endpoints_brewery_api(endpoint, schema):
    response = requests.get(endpoint)
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)


@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.parametrize("brewery_id", brewery_id, ids=brewery_id)
def test_get_brewery(brewery_id):
    response = requests.get(f"{BASE_URL_2}/breweries/{brewery_id}")
    data = response.json()
    assert response.status_code == 200
    assert brewery_id == data["id"]


@pytest.mark.smoke
@pytest.mark.regress
def test_brewery_size():
    size = randint(1, 50)
    response = requests.get(f"{BASE_URL_2}/breweries/random?size={size}")
    data = response.json()
    assert response.status_code == 200
    assert len(data) == size


@pytest.mark.regress
@pytest.mark.parametrize("filter, value, key", [
    ("by_name", "1", "name"),
    ("by_city", "oP", "city"),
    ("by_state", "Y", "state"),
    ("by_postal", "45", "postal_code"),
    ("by_type", choice(brewery_types), "brewery_type")
])
def test_brewery_filters(filter, value, key):
    response = requests.get(f"{BASE_URL_2}/breweries", params={filter: value})
    assert response.status_code == 200
    data = response.json()
    assert len(data) != 0
    for i in range(len(data)):
        assert value.lower() in data[i][key].lower()
