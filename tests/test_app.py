import pytest
from app import app, lists_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    lists_db.clear()
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_task_to_list(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    response = client.post('/lists/1/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data

def test_toggle_task_completion(client):
    client.post('/lists', data={'name': 'Chores'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'description': 'Clean room'}, follow_redirects=True)
    
    # Toggle task to complete
    response = client.post('/lists/1/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert lists_db[1]['tasks'][0]['completed'] is True
    
    # Toggle task back to incomplete
    response = client.post('/lists/1/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert lists_db[1]['tasks'][0]['completed'] is False

def test_delete_task(client):
    client.post('/lists', data={'name': 'Temp'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'description': 'Temp task'}, follow_redirects=True)
    response = client.post('/lists/1/tasks/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temp task' not in response.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Old List'}, follow_redirects=True)
    response = client.post('/lists/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Old List' not in response.data
