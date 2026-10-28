import pytest
from app import app, lists_store

@pytest.fixture
def client():
    app.config['TESTING'] = True
    lists_store.clear()
    with app.test_client() as client:
        yield client

def test_index_empty(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'No lists created yet' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data
    assert len(lists_store) == 1
