import pytest
from app import app, lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists.clear()
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_create_list_success(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data
    assert b'To-do list created successfully!' in response.data

def test_add_task_success(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    response = client.post('/lists/1/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data
    assert b'Task added successfully!' in response.data

def test_delete_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    response = client.post('/lists/1/tasks/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Task deleted successfully!' in response.data
    assert b'Finish report' not in response.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    response = client.post('/lists/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'To-do list deleted successfully!' in response.data
    assert b'Work' not in response.data
