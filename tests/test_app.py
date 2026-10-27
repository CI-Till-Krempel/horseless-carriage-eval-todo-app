import pytest
from app import app, lists_db, tasks_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists_db.clear()
        tasks_db.clear()
        yield client

def test_index_and_create_list(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do Lists' in response.data

    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data
