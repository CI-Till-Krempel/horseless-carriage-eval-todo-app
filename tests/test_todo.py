import pytest
from app import app, todo_lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    todo_lists.clear()
    with app.test_client() as client:
        yield client

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Work Tasks'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Work Tasks' in response.data

def test_add_and_toggle_task(client):
    client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    # List ID 1 should be created
    response = client.post('/lists/1/tasks', data={'text': 'Buy milk'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy milk' in response.data

    # Toggle complete
    response = client.post('/lists/1/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'class="completed"' in response.data

    # Toggle back incomplete
    response = client.post('/lists/1/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'class="completed"' not in response.data

def test_delete_task(client):
    client.post('/lists', data={'name': 'Temp List'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'text': 'Task to delete'}, follow_redirects=True)
    response = client.post('/lists/1/tasks/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Task to delete' not in response.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Doomed List'}, follow_redirects=True)
    response = client.post('/lists/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Doomed List' not in response.data
