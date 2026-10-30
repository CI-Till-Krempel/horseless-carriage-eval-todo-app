import pytest
from app import app, todos

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        todos.clear()
        yield client

def test_index_and_create_list(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do Lists' in response.data

    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data
    assert len(todos) == 1
    assert list(todos.values())[0]['name'] == 'Groceries'

def test_add_task_to_list(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    list_id = list(todos.keys())[0]

    response = client.post(f'/lists/{list_id}/tasks', data={'text': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data
    assert len(todos[list_id]['tasks']) == 1
    assert todos[list_id]['tasks'][0]['text'] == 'Finish report'
