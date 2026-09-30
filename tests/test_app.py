import os
import pytest
from app import app, DATA_FILE

@pytest.fixture
def client():
    app.config['TESTING'] = True
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    with app.test_client() as client:
        yield client
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

def test_index_and_create_list(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_and_toggle_and_delete_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    
    # Add task
    response = client.post('/lists/1/tasks', data={'content': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data

    # Toggle task
    response = client.post('/lists/1/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'completed' in response.data or b'Mark Incomplete' in response.data

    # Delete task
    response = client.post('/lists/1/tasks/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' not in response.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Temp List'}, follow_redirects=True)
    response = client.post('/lists/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temp List' not in response.data
