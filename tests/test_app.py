import pytest
from app import app, lists_store, tasks_store

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        lists_store.clear()
        tasks_store.clear()
        yield client

def test_index_and_create_list(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data
    assert b'(0/0 completed)' in response.data

def test_empty_list_validation(client):
    response = client.post('/lists', data={'name': ''}, follow_redirects=True)
    assert response.status_code == 200
    assert b'List name cannot be empty.' in response.data

def test_add_task_and_toggle_and_delete(client):
    # Create list first
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    list_id = list(lists_store.keys())[0]

    # Add task
    response = client.post(f'/lists/{list_id}/tasks', data={'text': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data
    task_id = list(tasks_store.keys())[0]

    # Toggle complete
    response = client.post(f'/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert tasks_store[task_id]['completed'] is True
    assert b'completed' in response.data

    # Delete task
    response = client.post(f'/tasks/{task_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' not in response.data
    assert len(tasks_store) == 0

def test_empty_task_validation(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    list_id = list(lists_store.keys())[0]
    response = client.post(f'/lists/{list_id}/tasks', data={'text': ''}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Task description cannot be empty.' in response.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Temp List'}, follow_redirects=True)
    list_id = list(lists_store.keys())[0]
    client.post(f'/lists/{list_id}/tasks', data={'text': 'Temp Task'}, follow_redirects=True)
    assert len(lists_store) == 1
    assert len(tasks_store) == 1

    response = client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temp List' not in response.data
    assert len(lists_store) == 0
    assert len(tasks_store) == 0
