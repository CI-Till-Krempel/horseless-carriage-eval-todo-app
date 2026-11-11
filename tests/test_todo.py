import pytest
from app import app, lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists.clear()
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists', json={'name': 'Work Tasks'}, headers={'Accept': 'application/json'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Work Tasks'
    assert data['id'] in lists
