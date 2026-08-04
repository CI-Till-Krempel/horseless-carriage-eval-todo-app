import pytest
from app import app, lists_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists_db.clear()
        yield client

def test_index_empty(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do List Web App' in response.data

def test_create_and_manage_list_and_tasks(client):
    # Create list
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

    # Add task
    response = client.post('/lists/1/tasks', data={'description': 'Buy milk'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy milk' in response.data

    # Toggle task complete
    response = client.post('/lists/1/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'completed' in response.data or b'Mark Incomplete' in response.data

    # Delete task
    response = client.post('/lists/1/tasks/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy milk' not in response.data

    # Delete list
    response = client.post('/lists/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' not in response.data
