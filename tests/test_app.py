import pytest
from app import app, todo_lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    todo_lists.clear()
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_create_list_add_task_and_toggle(client):
    # Create list
    response = client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Work' in response.data

    list_id = list(todo_lists.keys())[0]

    # Add task
    response = client.post(f'/lists/{list_id}/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data

    task_id = todo_lists[list_id]['tasks'][0]['id']
    assert todo_lists[list_id]['tasks'][0]['completed'] is False

    # Toggle task to complete
    response = client.post(f'/lists/{list_id}/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert todo_lists[list_id]['tasks'][0]['completed'] is True
    assert b'Mark Incomplete' in response.data
