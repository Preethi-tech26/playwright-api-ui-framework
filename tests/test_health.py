import pytest

BASE_URL = "https://restful-booker.herokuapp.com"

def test_health_check(api_context):
    response = api_context.get("/ping")
    assert response.status == 201