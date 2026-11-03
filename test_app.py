import pytest
from app import app, lists_store

@pytest.fixture
def client():
    app.config['TESTING'] = True
    lists_store.clear()
    with app.test_client() as client:
        yield client

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_create_list_json(client):
    response = client.post('/lists', json={'name': 'Work Tasks'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Work Tasks'
    assert data['id'] in lists_store
