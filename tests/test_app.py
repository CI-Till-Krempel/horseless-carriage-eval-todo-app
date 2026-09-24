import pytest
from app import app, todo_lists, tasks

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Clear state before each test
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

def test_task_lifecycle(client):
    # Create list
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    list_id = list(todo_lists.keys())[0]

    # Add task
    response = client.post(f'/lists/{list_id}/tasks', data={'text': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data
    assert len(tasks) == 1

    task_id = list(tasks.keys())[0]
    assert tasks[task_id]['completed'] is False

    # Toggle task
    client.post(f'/tasks/{task_id}/toggle', follow_redirects=True)
    assert tasks[task_id]['completed'] is True

    # Delete task
    client.post(f'/tasks/{task_id}/delete', follow_redirects=True)
    assert len(tasks) == 0
