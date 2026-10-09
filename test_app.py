import os
import tempfile
import pytest
from app import app
from models import DATA_FILE, TaskManager

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    
    # Use temporary file for test data
    global DATA_FILE
    import models
    models.DATA_FILE = app.config['DATABASE']

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_index_route(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'My To-Do Lists' in rv.data

def test_create_list(client):
    rv = client.post('/lists', data=dict(name='Groceries'), follow_redirects=True)
    assert rv.status_code == 200
    assert b'Groceries' in rv.data

def test_add_task(client):
    lst = TaskManager.create_list('Work')
    rv = client.post(f'/lists/{lst["id"]}/tasks', data=dict(description='Finish report'), follow_redirects=True)
    assert rv.status_code == 200
    assert b'Finish report' in rv.data

def test_toggle_task(client):
    lst = TaskManager.create_list('Home')
    task = TaskManager.add_task(lst['id'], 'Clean room')
    assert task['completed'] is False
    
    rv = client.post(f'/lists/{lst["id"]}/tasks/{task["id"]}/toggle', follow_redirects=True)
    assert rv.status_code == 200
    
    updated_lst = TaskManager.get_list(lst['id'])
    assert updated_lst['tasks'][0]['completed'] is True

def test_delete_task(client):
    lst = TaskManager.create_list('Personal')
    task = TaskManager.add_task(lst['id'], 'Buy milk')
    
    rv = client.post(f'/lists/{lst["id"]}/tasks/{task["id"]}/delete', follow_redirects=True)
    assert rv.status_code == 200
    
    updated_lst = TaskManager.get_list(lst['id'])
    assert len(updated_lst['tasks']) == 0

def test_delete_list(client):
    lst = TaskManager.create_list('Temporary')
    assert TaskManager.get_list(lst['id']) is not None
    
    rv = client.post(f'/lists/{lst["id"]}/delete', follow_redirects=True)
    assert rv.status_code == 200
    
    assert TaskManager.get_list(lst['id']) is None
