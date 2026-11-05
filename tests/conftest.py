import pytest

@pytest.fixture
def api_client():
    # Setup test client for API content-type negotiation (JSON vs redirect)
    try:
        from app import app
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client
    except ImportError:
        yield None
