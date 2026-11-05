import pytest
from app import app, todo_lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        todo_lists.clear()
        yield client

def test_add_task_to_list(client):
    # Create a list first
    response = client.post('/lists', data={'title': 'Test List'}, follow_redirects=True)
    assert response.status_code == 200
    assert len(todo_lists) == 1
    list_id = list(todo_lists.keys())[0]

    # Add task
    response = client.post(f'/lists/{list_id}/tasks', data={'description': 'Test Task'}, follow_redirects=True)
    assert response.status_code == 200
    assert len(todo_lists[list_id]['tasks']) == 1
    assert todo_lists[list_id]['tasks'][0]['description'] == 'Test Task'
