import pytest
from app import app

@pytest.fixture(autouse=True)
def reset_global_state():
    # Reset in-memory data structures before and after each test if available
    try:
        import app as app_module
        if hasattr(app_module, 'lists'):
            app_module.lists.clear()
        if hasattr(app_module, 'todos'):
            app_module.todos.clear()
    except Exception:
        pass
    yield
    try:
        import app as app_module
        if hasattr(app_module, 'lists'):
            app_module.lists.clear()
        if hasattr(app_module, 'todos'):
            app_module.todos.clear()
    except Exception:
        pass

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
