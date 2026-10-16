import pytest
from app import app, lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists.clear()
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data
    assert len(lists) == 1

def test_add_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    list_id = list(lists.keys())[0]
    response = client.post(f'/lists/{list_id}/tasks', data={'text': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data
    assert len(lists[list_id]['tasks']) == 1

def test_toggle_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    list_id = list(lists.keys())[0]
    client.post(f'/lists/{list_id}/tasks', data={'text': 'Finish report'}, follow_redirects=True)
    task_id = lists[list_id]['tasks'][0]['id']
    
    response = client.post(f'/lists/{list_id}/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert lists[list_id]['tasks'][0]['completed'] is True

def test_delete_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    list_id = list(lists.keys())[0]
    client.post(f'/lists/{list_id}/tasks', data={'text': 'Finish report'}, follow_redirects=True)
    task_id = lists[list_id]['tasks'][0]['id']
    
    response = client.post(f'/lists/{list_id}/tasks/{task_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert len(lists[list_id]['tasks']) == 0

def test_delete_list(client):
    client.post('/lists', data={'name': 'Temporary'}, follow_redirects=True)
    list_id = list(lists.keys())[0]
    response = client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert len(lists) == 0
