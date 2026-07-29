import pytest
from app import app, todo_lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    todo_lists.clear()
    with app.test_client() as client:
        yield client

def test_delete_entire_list(client):
    # Create list
    client.post('/lists', data={'name': 'Personal'}, follow_redirects=True)
    list_id = list(todo_lists.keys())[0]

    # Add task
    client.post(f'/lists/{list_id}/tasks', data={'description': 'Walk dog'}, follow_redirects=True)
    assert len(todo_lists) == 1

    # Delete entire list
    response = client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert len(todo_lists) == 0
    assert b'Personal' not in response.data
    assert b'Walk dog' not in response.data
