import pytest
from app import app, reset_store, todo_lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        reset_store()
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    list_id = list(todo_lists.keys())[0]
    response = client.post(f'/lists/{list_id}/tasks', data={'title': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data

def test_toggle_task(client):
    client.post('/lists', data={'name': 'Personal'}, follow_redirects=True)
    list_id = list(todo_lists.keys())[0]
    client.post(f'/lists/{list_id}/tasks', data={'title': 'Buy milk'}, follow_redirects=True)
    task_id = todo_lists[list_id]['tasks'][0]['id']
    
    response = client.post(f'/lists/{list_id}/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'Incomplete' in response.data
    
    response = client.post(f'/lists/{list_id}/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'Complete' in response.data

def test_delete_task(client):
    client.post('/lists', data={'name': 'Errands'}, follow_redirects=True)
    list_id = list(todo_lists.keys())[0]
    client.post(f'/lists/{list_id}/tasks', data={'title': 'Pick up dry cleaning'}, follow_redirects=True)
    task_id = todo_lists[list_id]['tasks'][0]['id']
    
    response = client.post(f'/lists/{list_id}/tasks/{task_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Pick up dry cleaning' not in response.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Temporary List'}, follow_redirects=True)
    list_id = list(todo_lists.keys())[0]
    
    response = client.post(f'/lists/{list_id}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temporary List' not in response.data
