import os
import sys
import pytest

# Add current directory to sys.path so app can be imported cleanly
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/..'))

from app import app, lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists.clear()
        import app as app_module
        app_module.next_list_id = 1
        app_module.next_task_id = 1
        yield client

def test_index_empty(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'No to-do lists yet' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data
    assert len(lists) == 1

def test_add_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    list_id = list(lists.keys())[0]
    
    response = client.post(f'/lists/{list_id}/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data
    assert len(lists[list_id]['tasks']) == 1

def test_toggle_task(client):
    client.post('/lists', data={'name': 'Chores'}, follow_redirects=True)
    list_id = list(lists.keys())[0]
    client.post(f'/lists/{list_id}/tasks', data={'description': 'Clean room'}, follow_redirects=True)
    task_id = lists[list_id]['tasks'][0]['id']
    
    # Toggle complete
    response = client.post(f'/lists/{list_id}/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert lists[list_id]['tasks'][0]['completed'] is True
    assert b'Mark Incomplete' in response.data

    # Toggle incomplete
    response = client.post(f'/lists/{list_id}/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert lists[list_id]['tasks'][0]['completed'] is False

def test_delete_task(client):
    client.post('/lists', data={'name': 'Personal'}, follow_redirects=True)
    list_id = list(lists.keys())[0]
    client.post(f'/lists/{list_id}/tasks', data={'description': 'Buy milk'}, follow_redirects=True)
    task_id = lists[list_id]['tasks'][0]['id']
    
    response = client.post(f'/lists/{list_id}/tasks/{task_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert len(lists[list_id]['tasks']) == 0
    assert b'Buy milk' not in response.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Temporary List'}, follow_redirects=True)
    list_id = list(lists.keys())[0]
    
    response = client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert len(lists) == 0
    assert b'Temporary List' not in response.data
