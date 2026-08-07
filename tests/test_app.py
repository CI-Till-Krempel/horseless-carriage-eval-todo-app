import pytest
from app import app, lists_store

@pytest.fixture
def client():
    app.config['TESTING'] = True
    lists_store.clear()
    with app.test_client() as client:
        yield client

def test_index_empty(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'No to-do lists created yet' in response.data

def test_create_list_and_tasks_workflow(client):
    # 1. Create list
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

    # Find list id
    list_id = list(lists_store.keys())[0]

    # 2. Add task
    response = client.post(f'/lists/{list_id}/tasks', data={'text': 'Buy milk'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy milk' in response.data

    task_id = lists_store[list_id]["tasks"][0]["id"]

    # 3. Toggle task completion
    response = client.post(f'/lists/{list_id}/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert lists_store[list_id]["tasks"][0]["completed"] is True

    # 4. Delete task
    response = client.post(f'/lists/{list_id}/tasks/{task_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert len(lists_store[list_id]["tasks"]) == 0

    # 5. Delete list
    response = client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert len(lists_store) == 0
