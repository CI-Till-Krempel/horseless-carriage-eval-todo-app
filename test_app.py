import pytest
from app import app, todo_lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        todo_lists.clear()
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
    assert todo_lists[0]['name'] == 'Groceries'

def test_add_task_to_list(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    response = client.post('/lists/1/tasks', data={'content': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data
    assert len(todo_lists[0]['tasks']) == 1
    assert todo_lists[0]['tasks'][0]['content'] == 'Finish report'
    assert todo_lists[0]['tasks'][0]['completed'] is False

def test_toggle_task_completion(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'content': 'Finish report'}, follow_redirects=True)
    
    # Toggle complete
    response = client.post('/lists/1/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert todo_lists[0]['tasks'][0]['completed'] is True
    
    # Toggle incomplete again
    response = client.post('/lists/1/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert todo_lists[0]['tasks'][0]['completed'] is False
