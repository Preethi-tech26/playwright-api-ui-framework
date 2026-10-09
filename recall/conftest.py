
import pytest

BASE_URL="https://restful-booker.herokuapp.com"

@pytest.fixture
def api_context(playwright):
    request_context = playwright.request.new_context(base_url = BASE_URL)
    yield request_context
    request_context.dispose()
 
 
