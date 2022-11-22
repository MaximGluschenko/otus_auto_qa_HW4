import pytest
import requests
from jsonschema import validate
from data_for_test_3 import ENDPOINTS_3
from schemas_3 import SCHEMA_1, SCHEMA_2, SCHEMA_3


@pytest.mark.smoke
@pytest.mark.parametrize("endpoint", ENDPOINTS_3.values(), ids=ENDPOINTS_3.keys())
def test_endpoints_status_jsonplaceholder_api(endpoint):
    response = requests.get(endpoint)
    data = response.json()
    assert response.status_code == 200
    assert len(data) != 0


@pytest.mark.smoke
@pytest.mark.parametrize("endpoint, schema", [
    (ENDPOINTS_3["Getting a resource"], SCHEMA_1),
    (ENDPOINTS_3["Listing all resources"], SCHEMA_2),
    (ENDPOINTS_3["Listing nested comments"], SCHEMA_3)
])
def test_validate_endpoints_jsonplaceholder_api(endpoint, schema):
    response = requests.get(endpoint)
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)


@pytest.mark.smoke
@pytest.mark.regress
def test_post_method_jsonplaceholder_api():
    response = requests.post(ENDPOINTS_3["Listing all resources"])
    data = response.json()
    assert response.status_code == 201
    assert len(data) != 0


@pytest.mark.smoke
@pytest.mark.regress
def test_put_method_jsonplaceholder_api():
    response = requests.put(ENDPOINTS_3["Getting a resource"])
    data = response.json()
    assert response.status_code == 200
    assert len(data) != 0


@pytest.mark.smoke
@pytest.mark.regress
def test_delete_method_jsonplaceholder_api():
    response = requests.delete(ENDPOINTS_3["Getting a resource"])
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 0
