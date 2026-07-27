import pytest
from app import app, lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists.clear()
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists/create', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_and_toggle_task(client):
    client.post('/lists/create', data={'name': 'Work'}, follow_redirects=True)
    list_id = 1
    response = client.post(f'/lists/{list_id}/tasks/add', data={'text': 'Write docs'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Write docs' in response.data

    # Toggle task
    response = client.post(f'/lists/{list_id}/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'completed' in response.data or b'Mark Incomplete' in response.data

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
