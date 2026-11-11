import pytest
from app import app, todo_lists

@pytest.fixture(autouse=True)
def clear_lists():
    todo_lists.clear()
    global next_list_id, next_task_id
    import app
    app.next_list_id = 1
    app.next_task_id = 1

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Work Tasks'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Work Tasks' in response.data

def test_add_and_toggle_task(client):
    client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    list_id = list(todo_lists.keys())[0]
    
    response = client.post(f'/lists/{list_id}/tasks', data={'text': 'Buy milk'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy milk' in response.data

    task_id = todo_lists[list_id]['tasks'][0]['id']

    # Toggle complete
    response = client.post(f'/lists/{list_id}/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'class="completed"' in response.data

    # Toggle back incomplete
    response = client.post(f'/lists/{list_id}/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'class="completed"' not in response.data

def test_delete_task(client):
    client.post('/lists', data={'name': 'Temp List'}, follow_redirects=True)
    list_id = list(todo_lists.keys())[0]
    client.post(f'/lists/{list_id}/tasks', data={'text': 'Task to delete'}, follow_redirects=True)
    task_id = todo_lists[list_id]['tasks'][0]['id']
    
    response = client.post(f'/lists/{list_id}/tasks/{task_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Task to delete' not in response.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Doomed List'}, follow_redirects=True)
    list_id = list(todo_lists.keys())[0]
    response = client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Doomed List' not in response.data
