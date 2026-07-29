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

def test_create_list_and_add_task(client):
    # Create list
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

    # Add task
    # Find the generated list ID
    list_id = list(todo_lists.keys())[0]
    response = client.post(f'/lists/{list_id}/tasks', data={'description': 'Buy milk'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy milk' in response.data
