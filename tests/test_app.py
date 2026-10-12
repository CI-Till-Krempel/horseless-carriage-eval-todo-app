import pytest
from app import app, lists_db, tasks_db

@pytest.fixture
def client():
    lists_db.clear()
    tasks_db.clear()
    return app.test_client()

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_task_to_list(client):
    client.post('/lists', data={'name': 'Work'})
    list_id = list(lists_db.keys())[0]
    response = client.post(f'/lists/{list_id}/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data

def test_toggle_task(client):
    client.post('/lists', data={'name': 'Home'})
    list_id = list(lists_db.keys())[0]
    client.post(f'/lists/{list_id}/tasks', data={'description': 'Clean room'})
    task_id = list(tasks_db.keys())[0]
    assert tasks_db[task_id]['completed'] is False
    
    response = client.post(f'/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert tasks_db[task_id]['completed'] is True

def test_delete_task(client):
    client.post('/lists', data={'name': 'School'})
    list_id = list(lists_db.keys())[0]
    client.post(f'/lists/{list_id}/tasks', data={'description': 'Read book'})
    task_id = list(tasks_db.keys())[0]
    assert task_id in tasks_db
    
    response = client.post(f'/tasks/{task_id}', data={'_method': 'DELETE'}, follow_redirects=True)
    assert response.status_code == 200
    assert task_id not in tasks_db

def test_delete_list_cascade(client):
    client.post('/lists', data={'name': 'ProjectX'})
    list_id = list(lists_db.keys())[0]
    client.post(f'/lists/{list_id}/tasks', data={'description': 'Task 1'})
    task_id = list(tasks_db.keys())[0]
    assert list_id in lists_db
    assert task_id in tasks_db
    
    response = client.post(f'/lists/{list_id}', data={'_method': 'DELETE'}, follow_redirects=True)
    assert response.status_code == 200
    assert list_id not in lists_db
    assert task_id not in tasks_db
