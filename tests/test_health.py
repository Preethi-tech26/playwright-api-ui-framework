import pytest

BASE_URL = "https://restful-booker.herokuapp.com"

def test_health_check(playwright):
    request_context = playwright.request.new_context(base_url=BASE_URL)
    response = request_context.get("/ping")
    assert response.status == 201
    request_context.dispose()