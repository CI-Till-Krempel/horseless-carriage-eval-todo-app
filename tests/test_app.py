import pytest
from app import app, lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists.clear()
        yield client

def test_index_empty(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_task_and_view(client):
    # Create list
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    # Add task
    response = client.post('/lists/1/tasks', data={'text': 'Write unit tests'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Write unit tests' in response.data

def test_toggle_and_delete_task(client):
    client.post('/lists', data={'name': 'Personal'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'text': 'Buy milk'}, follow_redirects=True)
    
    # Toggle task complete
    response = client.post('/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'completed' in response.data or b'class="completed"' in response.data

    # Delete task
    response = client.post('/tasks/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy milk' not in response.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Temp List'}, follow_redirects=True)
    response = client.post('/lists/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temp List' not in response.data
