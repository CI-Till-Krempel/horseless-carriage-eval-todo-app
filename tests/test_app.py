import pytest
from app import app, todo_lists, tasks

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        todo_lists.clear()
        tasks.clear()
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do Lists' in response.data

def test_create_and_delete_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data
    assert len(todo_lists) == 1

    list_id = list(todo_lists.keys())[0]
    response = client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' not in response.data
    assert len(todo_lists) == 0

def test_empty_list_validation(client):
    response = client.post('/lists', data={'name': '   '}, follow_redirects=True)
    assert response.status_code == 200
    assert b'List name cannot be empty.' in response.data
    assert len(todo_lists) == 0

def test_task_lifecycle(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    list_id = list(todo_lists.keys())[0]

    response = client.post(f'/lists/{list_id}/tasks', data={'text': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data
    assert len(tasks) == 1

    task_id = list(tasks.keys())[0]
    assert tasks[task_id]['completed'] is False

    client.post(f'/tasks/{task_id}/toggle', follow_redirects=True)
    assert tasks[task_id]['completed'] is True

    client.post(f'/tasks/{task_id}/delete', follow_redirects=True)
    assert len(tasks) == 0

def test_empty_task_validation(client):
    client.post('/lists', data={'name': 'Personal'}, follow_redirects=True)
    list_id = list(todo_lists.keys())[0]

    response = client.post(f'/lists/{list_id}/tasks', data={'text': ''}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Task description cannot be empty.' in response.data
    assert len(tasks) == 0
