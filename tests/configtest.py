import pytest


@pytest.fixture(scope="session")
def login_details(request):
    return request.param

