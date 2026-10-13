import os
import pytest
from app import app, init_db, DB_NAME

@pytest.fixture
def client():
    app.config['TESTING'] = True
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
    init_db()
    with app.test_client() as client:
        yield client
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Work Tasks'}, headers={'Accept': 'application/json'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Work Tasks'
    assert 'id' in data

def test_add_task_and_toggle_and_delete(client):
    # Create list
    res = client.post('/lists', data={'name': 'Groceries'}, headers={'Accept': 'application/json'})
    list_id = res.get_json()['id']

    # Add task
    res_task = client.post(f'/lists/{list_id}/tasks', data={'description': 'Buy milk'}, headers={'Accept': 'application/json'})
    assert res_task.status_code == 201
    task_id = res_task.get_json()['id']

    # Check index shows task
    index_res = client.get('/')
    assert b'Buy milk' in index_res.data

    # Toggle completion
    toggle_res = client.post(f'/tasks/{task_id}/toggle', follow_redirects=True)
    assert toggle_res.status_code == 200

    # Delete task
    del_res = client.post(f'/tasks/{task_id}/delete', follow_redirects=True)
    assert del_res.status_code == 200

def test_delete_list(client):
    res = client.post('/lists', data={'name': 'Temp List'}, headers={'Accept': 'application/json'})
    list_id = res.get_json()['id']

    del_res = client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert del_res.status_code == 200
    assert b'Temp List' not in client.get('/').data
