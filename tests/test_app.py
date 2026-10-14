import pytest
from app import app, todo_lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        todo_lists.clear()
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'To-Do Lists' in rv.data

def test_create_list(client):
    rv = client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    assert rv.status_code == 200
    assert b'Work' in rv.data

def test_add_and_complete_task(client):
    client.post('/lists', data={'name': 'Personal'}, follow_redirects=True)
    list_id = list(todo_lists.keys())[0]
    
    rv = client.post(f'/lists/{list_id}/tasks', data={'description': 'Buy milk'}, follow_redirects=True)
    assert rv.status_code == 200
    assert b'Buy milk' in rv.data
    
    task_id = list(todo_lists[list_id]['tasks'].keys())[0]
    rv = client.post(f'/lists/{list_id}/tasks/{task_id}/toggle', follow_redirects=True)
    assert rv.status_code == 200
    assert b'completed' in rv.data or b'Mark Incomplete' in rv.data
