import pytest
import os
import json
import app as flask_app

@pytest.fixture
def client():
    flask_app.app.config['TESTING'] = True
    if os.path.exists(flask_app.DATA_FILE):
        os.remove(flask_app.DATA_FILE)
    flask_app.lists.clear()
    flask_app.list_id_counter = 1
    flask_app.task_id_counter = 1
    with flask_app.app.test_client() as client:
        yield client
    if os.path.exists(flask_app.DATA_FILE):
        os.remove(flask_app.DATA_FILE)

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_create_list_persistence(client):
    response = client.post('/lists/create', data={'name': 'Persistent List'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Persistent List' in response.data
    
    # Verify data.json was created and populated
    assert os.path.exists(flask_app.DATA_FILE)
    with open(flask_app.DATA_FILE, 'r') as f:
        data = json.load(f)
        assert len(data['lists']) == 1
        assert data['lists'][0]['name'] == 'Persistent List'

def test_add_and_toggle_task(client):
    client.post('/lists/create', data={'name': 'Work'}, follow_redirects=True)
    list_id = 1
    client.post(f'/lists/{list_id}/tasks/add', data={'text': 'Write docs'}, follow_redirects=True)
    
    # Toggle task
    response = client.post(f'/lists/{list_id}/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    
    # Verify persistence file reflects toggle
    with open(flask_app.DATA_FILE, 'r') as f:
        data = json.load(f)
        assert data['lists'][0]['tasks'][0]['completed'] is True

def test_delete_task(client):
    client.post('/lists/create', data={'name': 'Work'}, follow_redirects=True)
    client.post('/lists/1/tasks/add', data={'text': 'Temp Task'}, follow_redirects=True)
    response = client.post('/lists/1/tasks/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temp Task' not in response.data

def test_delete_list(client):
    client.post('/lists/create', data={'name': 'Obsolete List'}, follow_redirects=True)
    response = client.post('/lists/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Obsolete List' not in response.data
