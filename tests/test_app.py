import pytest
from app import app, todo_lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        todo_lists.clear()
        yield client

def test_index_and_create_list(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do Lists' in response.data

    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data
    assert 'Groceries' in todo_lists
