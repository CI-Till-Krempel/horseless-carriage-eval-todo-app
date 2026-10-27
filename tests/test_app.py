import pytest
from app import app, lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    lists.clear()
    response = client.get('/')
    assert response.status_code == 200
