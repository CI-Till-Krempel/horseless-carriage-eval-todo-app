import pytest
from app import app, lists_db, tasks_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists_db.clear()
        tasks_db.clear()
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_add_list_and_task(client):
    response = client.post('/list/create', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

    response = client.post('/list/1/task/add', data={'description': 'Buy milk'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy milk' in response.data

def test_toggle_task(client):
    client.post('/list/create', data={'name': 'Work'}, follow_redirects=True)
    client.post('/list/1/task/add', data={'description': 'Write code'}, follow_redirects=True)
    
    response = client.post('/list/1/task/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'text-decoration: line-through' in response.data

def test_delete_task(client):
    client.post('/list/create', data={'name': 'Personal'}, follow_redirects=True)
    client.post('/list/1/task/add', data={'description': 'Clean room'}, follow_redirects=True)
    
    response = client.post('/list/1/task/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Clean room' not in response.data

def test_delete_list(client):
    client.post('/list/create', data={'name': 'Temp List'}, follow_redirects=True)
    client.post('/list/1/task/add', data={'description': 'Temp task'}, follow_redirects=True)
    
    response = client.post('/list/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temp List' not in response.data
    assert b'Temp task' not in response.data
