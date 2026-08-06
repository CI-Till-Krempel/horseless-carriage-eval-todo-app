import pytest
from app import app, todos_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    todos_db.clear()
    with app.test_client() as client:
        yield client

def test_index_empty(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'No to-do lists yet' in response.data

def test_create_and_view_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_and_view_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    # list_id should be 1
    response = client.post('/lists/1/tasks', data={'text': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data

def test_toggle_task(client):
    client.post('/lists', data={'name': 'Home'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'text': 'Clean room'}, follow_redirects=True)
    # toggle task 1
    response = client.post('/lists/1/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'completed' in response.data

def test_delete_task(client):
    client.post('/lists', data={'name': 'Chores'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'text': 'Wash dishes'}, follow_redirects=True)
    response = client.post('/lists/1/tasks/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Wash dishes' not in response.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Temporary'}, follow_redirects=True)
    assert b'Temporary' in response.data
    response = client.post('/lists/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temporary' not in response.data
