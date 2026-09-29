import pytest
from app import app, todo_lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        todo_lists.clear()
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    response = client.post('/lists/1/tasks', data={'title': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data

def test_toggle_task(client):
    client.post('/lists', data={'name': 'Personal'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'title': 'Buy milk'}, follow_redirects=True)
    
    # Toggle complete
    response = client.post('/lists/1/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'Mark Incomplete' in response.data
    
    # Toggle back to incomplete
    response = client.post('/lists/1/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'Mark Complete' in response.data
