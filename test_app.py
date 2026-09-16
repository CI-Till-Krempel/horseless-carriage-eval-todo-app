import pytest
from app import app, lists_db, tasks_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    lists_db.clear()
    tasks_db.clear()
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_create_list_and_add_task(client):
    # Create list
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

    # Add task
    response = client.post('/lists/1/tasks', data={'description': 'Buy milk'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy milk' in response.data

def test_toggle_and_delete_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'description': 'Finish report'}, follow_redirects=True)

    # Toggle task complete
    response = client.post('/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'line-through' in response.data

    # Delete task
    response = client.post('/tasks/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' not in response.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Personal'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'description': 'Exercise'}, follow_redirects=True)

    # Delete list
    response = client.post('/lists/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Personal' not in response.data
    assert b'Exercise' not in response.data
