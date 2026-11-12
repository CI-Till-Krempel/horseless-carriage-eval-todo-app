import pytest
from app import app, lists

@pytest.fixture(autouse=True)
def reset_global_state():
    # Reset in-memory data structures before each test
    lists.clear()
    yield
    lists.clear()

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
