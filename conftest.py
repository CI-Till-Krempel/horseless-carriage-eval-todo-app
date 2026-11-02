import pytest
from app import app, lists, tasks

@pytest.fixture(autouse=True)
def reset_app_state():
    lists.clear()
    tasks.clear()
    yield
    lists.clear()
    tasks.clear()

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
