import pytest
from app import app, lists, tasks

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    res = client.get('/')
    assert res.status_code == 200

def test_create_list_and_add_task(client):
    global lists, tasks
    lists.clear()
    tasks.clear()
    
    res = client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    assert res.status_code == 200
    assert b'Work' in res.data
    
    res = client.post('/lists/1/tasks', data={'title': 'Finish report'}, follow_redirects=True)
    assert res.status_code == 200
    assert b'Finish report' in res.data

def test_toggle_and_delete_task(client):
    global lists, tasks
    lists.clear()
    tasks.clear()
    
    lists.append({'id': 1, 'name': 'Personal'})
    tasks.append({'id': 1, 'list_id': 1, 'title': 'Buy milk', 'completed': False})
    
    res = client.post('/tasks/1/toggle', follow_redirects=True)
    assert res.status_code == 200
    assert tasks[0]['completed'] is True
    
    res = client.post('/tasks/1/delete', follow_redirects=True)
    assert res.status_code == 200
    assert len(tasks) == 0

def test_delete_list(client):
    global lists, tasks
    lists.clear()
    tasks.clear()
    
    lists.append({'id': 1, 'name': 'Temp'})
    tasks.append({'id': 1, 'list_id': 1, 'title': 'Task', 'completed': False})
    
    res = client.post('/lists/1/delete', follow_redirects=True)
    assert res.status_code == 200
    assert len(lists) == 0
    assert len(tasks) == 0
