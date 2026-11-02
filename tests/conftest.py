import pytest
from app import app, lists

@pytest.fixture(autouse=True)
def reset_lists():
    lists.clear()
    yield
    lists.clear()

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
