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
    assert b'My To-Do Lists' in response.data

def test_create_list_success(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data
    assert b'To-do list created successfully!' in response.data

def test_create_list_empty(client):
    response = client.post('/lists', data={'name': '   '}, follow_redirects=True)
    assert response.status_code == 200
    assert b'List name cannot be empty or whitespace.' in response.data
