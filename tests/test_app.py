import pytest
from app import app, todo_lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    todo_lists.clear()
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_crud_flow(client):
    # 1. Create list
    response = client.post('/lists', data={'name': 'Work Tasks'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Work Tasks' in response.data
    
    # Get list ID
    list_id = list(todo_lists.keys())[0]

    # 2. Add task
    response = client.post(f'/lists/{list_id}/tasks', data={'title': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data
    
    task_id = list(todo_lists[list_id]['tasks'].keys())[0]

    # 3. Toggle task completion
    response = client.post(f'/lists/{list_id}/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert todo_lists[list_id]['tasks'][task_id]['completed'] is True

    # 4. Delete task
    response = client.post(f'/lists/{list_id}/tasks/{task_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert len(todo_lists[list_id]['tasks']) == 0

    # 5. Delete list
    response = client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert len(todo_lists) == 0
