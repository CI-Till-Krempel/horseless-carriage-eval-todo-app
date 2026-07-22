import pytest
from app import app, lists_db, tasks_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    lists_db.clear()
    tasks_db.clear()
    return app.test_client()

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Work' in response.data

def test_add_and_toggle_and_delete_task(client):
    client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    list_id = list(lists_db.keys())[0]

    response = client.post(f'/lists/{list_id}/tasks', data={'text': 'Buy milk'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy milk' in response.data
    task_id = list(tasks_db.keys())[0]

    response = client.post(f'/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert tasks_db[task_id]['completed'] is True

    response = client.post(f'/tasks/{task_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert task_id not in tasks_db

def test_delete_list(client):
    client.post('/lists', data={'name': 'Temporary'}, follow_redirects=True)
    list_id = list(lists_db.keys())[0]
    client.post(f'/lists/{list_id}/tasks', data={'text': 'Temp task'}, follow_redirects=True)

    response = client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert list_id not in lists_db
    assert len(tasks_db) == 0
