import pytest
from app import app, todo_lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        todo_lists.clear()
        yield client

def test_add_task_to_list(client):
    response = client.post('/lists', data={'title': 'Test List'}, follow_redirects=True)
    assert response.status_code == 200
    assert len(todo_lists) == 1
    list_id = list(todo_lists.keys())[0]

    response = client.post(f'/lists/{list_id}/tasks', data={'description': 'Test Task'}, follow_redirects=True)
    assert response.status_code == 200
    assert len(todo_lists[list_id]['tasks']) == 1
    assert todo_lists[list_id]['tasks'][0]['description'] == 'Test Task'
    assert todo_lists[list_id]['tasks'][0]['completed'] is False

def test_toggle_task_completion(client):
    response = client.post('/lists', data={'title': 'Test List'}, follow_redirects=True)
    list_id = list(todo_lists.keys())[0]

    response = client.post(f'/lists/{list_id}/tasks', data={'description': 'Test Task'}, follow_redirects=True)
    task_id = todo_lists[list_id]['tasks'][0]['id']

    response = client.post(f'/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert todo_lists[list_id]['tasks'][0]['completed'] is True

def test_delete_task(client):
    response = client.post('/lists', data={'title': 'Test List'}, follow_redirects=True)
    list_id = list(todo_lists.keys())[0]

    response = client.post(f'/lists/{list_id}/tasks', data={'description': 'Test Task'}, follow_redirects=True)
    task_id = todo_lists[list_id]['tasks'][0]['id']

    response = client.post(f'/tasks/{task_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert len(todo_lists[list_id]['tasks']) == 0

def test_delete_list(client):
    response = client.post('/lists', data={'title': 'Test List'}, follow_redirects=True)
    list_id = list(todo_lists.keys())[0]

    response = client.post(f'/lists/{list_id}/tasks', data={'description': 'Test Task'}, follow_redirects=True)
    assert len(todo_lists) == 1

    response = client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert len(todo_lists) == 0
