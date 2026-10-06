import pytest
from app import app, lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    lists.clear()
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
    assert len(lists) == 1
    assert lists[0]['name'] == 'Groceries'

def test_add_and_toggle_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    list_id = lists[0]['id']
    client.post(f'/lists/{list_id}/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    assert len(lists[0]['tasks']) == 1
    task_id = lists[0]['tasks'][0]['id']
    assert lists[0]['tasks'][0]['completed'] is False
    
    # Toggle task to complete
    client.post(f'/lists/{list_id}/tasks/{task_id}/toggle', follow_redirects=True)
    assert lists[0]['tasks'][0]['completed'] is True

def test_delete_task(client):
    client.post('/lists', data={'name': 'Personal'}, follow_redirects=True)
    list_id = lists[0]['id']
    client.post(f'/lists/{list_id}/tasks', data={'description': 'Buy milk'}, follow_redirects=True)
    assert len(lists[0]['tasks']) == 1
    task_id = lists[0]['tasks'][0]['id']
    
    # Delete task
    client.post(f'/lists/{list_id}/tasks/{task_id}/delete', follow_redirects=True)
    assert len(lists[0]['tasks']) == 0

def test_delete_list(client):
    client.post('/lists', data={'name': 'Temporary'}, follow_redirects=True)
    assert len(lists) == 1
    list_id = lists[0]['id']
    
    # Delete list
    client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert len(lists) == 0
