import pytest
from app import app
import app as app_module

@pytest.fixture(autouse=True)
def clear_state():
    # Clear global state before and after each test using direct module references
    if hasattr(app_module, 'lists'):
        app_module.lists.clear()
    yield
    if hasattr(app_module, 'lists'):
        app_module.lists.clear()

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
