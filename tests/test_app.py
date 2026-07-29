import pytest
from app import app, todo_lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    todo_lists.clear()
    with app.test_client() as client:
        yield client

def test_delete_task(client):
    # Create list
    client.post('/lists', data={'name': 'Chores'}, follow_redirects=True)
    list_id = list(todo_lists.keys())[0]

    # Add task
    client.post(f'/lists/{list_id}/tasks', data={'description': 'Clean room'}, follow_redirects=True)
    task_id = todo_lists[list_id]['tasks'][0]['id']
    assert len(todo_lists[list_id]['tasks']) == 1

    # Delete task
    response = client.post(f'/lists/{list_id}/tasks/{task_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert len(todo_lists[list_id]['tasks']) == 0
    assert b'Clean room' not in response.data
