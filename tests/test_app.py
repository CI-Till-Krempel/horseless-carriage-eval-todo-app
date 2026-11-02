import pytest
from app import app, lists, tasks

@pytest.fixture
def client():
    app.config['TESTING'] = True
    lists.clear()
    tasks.clear()
    with app.test_client() as client:
        yield client

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data
    assert len(lists) == 1
    assert lists[0]['name'] == 'Groceries'

def test_add_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    list_id = lists[0]['id']
    response = client.post(f'/lists/{list_id}/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data
    assert len(tasks) == 1
    assert tasks[0]['description'] == 'Finish report'
    assert tasks[0]['completed'] == False

def test_toggle_task(client):
    client.post('/lists', data={'name': 'Chores'}, follow_redirects=True)
    list_id = lists[0]['id']
    client.post(f'/lists/{list_id}/tasks', data={'description': 'Clean room'}, follow_redirects=True)
    task_id = tasks[0]['id']
    
    # Toggle complete
    response = client.post(f'/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert tasks[0]['completed'] == True
    
    # Toggle incomplete
    response = client.post(f'/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert tasks[0]['completed'] == False

def test_delete_task(client):
    client.post('/lists', data={'name': 'Chores'}, follow_redirects=True)
    list_id = lists[0]['id']
    client.post(f'/lists/{list_id}/tasks', data={'description': 'Clean room'}, follow_redirects=True)
    assert len(tasks) == 1
    task_id = tasks[0]['id']
    
    response = client.post(f'/tasks/{task_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert len(tasks) == 0

def test_delete_list(client):
    client.post('/lists', data={'name': 'Obsolete List'}, follow_redirects=True)
    list_id = lists[0]['id']
    client.post(f'/lists/{list_id}/tasks', data={'description': 'Obsolete Task'}, follow_redirects=True)
    assert len(lists) == 1
    assert len(tasks) == 1
    
    response = client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert len(lists) == 0
    assert len(tasks) == 0
