import pytest
from app import app, lists_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists_db.clear()
        yield client

def test_index(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b'To-Do List App' in res.data

def test_create_list(client):
    res = client.post('/api/lists', json={'name': 'Groceries'})
    assert res.status_code == 201
    data = res.get_json()
    assert data['name'] == 'Groceries'
    assert data['id'] in lists_db

def test_add_task(client):
    # Create list first
    res = client.post('/api/lists', json={'name': 'Work'})
    list_id = res.get_json()['id']

    # Add task
    res2 = client.post(f'/api/lists/{list_id}/tasks', json={'description': 'Finish report'})
    assert res2.status_code == 201
    task_data = res2.get_json()
    assert task_data['description'] == 'Finish report'
    assert task_data['completed'] is False
    assert len(lists_db[list_id]['tasks']) == 1

def test_toggle_and_delete_task(client):
    res = client.post('/api/lists', json={'name': 'Home'})
    list_id = res.get_json()['id']

    res2 = client.post(f'/api/lists/{list_id}/tasks', json={'description': 'Clean room'})
    task_id = res2.get_json()['id']

    # Toggle complete
    res3 = client.patch(f'/api/lists/{list_id}/tasks/{task_id}/toggle')
    assert res3.status_code == 200
    assert res3.get_json()['completed'] is True

    # Delete task
    res4 = client.delete(f'/api/lists/{list_id}/tasks/{task_id}')
    assert res4.status_code == 200
    assert len(lists_db[list_id]['tasks']) == 0

def test_delete_list(client):
    res = client.post('/api/lists', json={'name': 'Temp'})
    list_id = res.get_json()['id']

    res2 = client.delete(f'/api/lists/{list_id}')
    assert res2.status_code == 200
    assert list_id not in lists_db
