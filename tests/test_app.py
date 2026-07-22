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

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data
    assert len(todo_lists) == 1

def test_add_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    list_id = list(todo_lists.keys())[0]
    response = client.post(f'/lists/{list_id}/tasks', data={'text': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data
    assert len(todo_lists[list_id]['tasks']) == 1
    assert todo_lists[list_id]['tasks'][0]['text'] == 'Finish report'
