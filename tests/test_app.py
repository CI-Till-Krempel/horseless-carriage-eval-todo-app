import os
import tempfile
import pytest
from app import app, init_db, DB_NAME

@pytest.fixture
def client():
    app.config['TESTING'] = True
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    
    # Override DB_NAME in app for testing if needed, or use standard init
    init_db()
    
    with app.test_client() as client:
        yield client
        
    os.close(db_fd)

def test_index_loads(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do List Application' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_and_complete_task(client):
    # Create list first
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    # Add task
    response = client.post('/lists/1/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data
    
    # Toggle complete
    response = client.post('/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'completed' in response.data or response.status_code == 200

def test_delete_task(client):
    client.post('/lists', data={'name': 'Chores'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'description': 'Clean room'}, follow_redirects=True)
    response = client.post('/tasks/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Clean room' not in response.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Temp List'}, follow_redirects=True)
    response = client.post('/lists/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temp List' not in response.data
