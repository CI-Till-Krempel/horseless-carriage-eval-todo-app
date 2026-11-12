import os
import tempfile
import pytest

import app as todo_app

@pytest.fixture
def client():
    db_fd, todo_app.DB_NAME = tempfile.mkstemp()
    todo_app.init_db()
    todo_app.app.config['TESTING'] = True

    with todo_app.app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(todo_app.DB_NAME)

def test_index_and_create_list(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do List Dashboard' in response.data

    response = client.post('/list/create', data={'name': 'Work Tasks'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Work Tasks' in response.data

def test_task_operations(client):
    client.post('/list/create', data={'name': 'Groceries'}, follow_redirects=True)
    
    # Add task
    response = client.post('/list/1/task/add', data={'description': 'Buy milk'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy milk' in response.data

    # Toggle task complete
    response = client.post('/task/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'completed' in response.data or b'Mark Incomplete' in response.data

    # Delete task
    response = client.post('/task/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy milk' not in response.data

def test_delete_list(client):
    client.post('/list/create', data={'name': 'Temp List'}, follow_redirects=True)
    response = client.post('/list/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temp List' not in response.data
