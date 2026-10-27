import pytest
from app import app, lists_store, list_counter, task_counter

@pytest.fixture
def client():
    app.config['TESTING'] = True
    lists_store.clear()
    global list_counter, task_counter
    list_counter = 1
    task_counter = 1
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    list_id = list(lists_store.keys())[0]
    response = client.post(f'/lists/{list_id}/tasks', data={'text': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data

def test_toggle_task(client):
    client.post('/lists', data={'name': 'Chores'}, follow_redirects=True)
    list_id = list(lists_store.keys())[0]
    client.post(f'/lists/{list_id}/tasks', data={'text': 'Clean room'}, follow_redirects=True)
    task_id = list(lists_store[list_id]['tasks'].keys())[0]
    response = client.post(f'/lists/{list_id}/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'completed' in response.data

def test_delete_task(client):
    client.post('/lists', data={'name': 'Chores'}, follow_redirects=True)
    list_id = list(lists_store.keys())[0]
    client.post(f'/lists/{list_id}/tasks', data={'text': 'Clean room'}, follow_redirects=True)
    task_id = list(lists_store[list_id]['tasks'].keys())[0]
    response = client.post(f'/lists/{list_id}/tasks/{task_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Clean room' not in response.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Obsolete'}, follow_redirects=True)
    list_id = list(lists_store.keys())[0]
    response = client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Obsolete' not in response.data
