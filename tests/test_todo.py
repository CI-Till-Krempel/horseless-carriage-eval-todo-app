import pytest
from app import app, lists_db, tasks_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Clear DB before each test
        lists_db.clear()
        tasks_db.clear()
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do List Web App' in response.data

def test_create_list(client):
    response = client.post('/lists', json={'name': 'Work Tasks'}, headers={'Accept': 'application/json'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Work Tasks'
    assert data['id'] in lists_db

def test_add_task_to_list(client):
    # Create list first
    res = client.post('/lists', json={'name': 'Personal'}, headers={'Accept': 'application/json'})
    list_id = res.get_json()['id']

    # Add task
    response = client.post(f'/lists/{list_id}/tasks', json={'description': 'Buy milk'}, headers={'Accept': 'application/json'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['description'] == 'Buy milk'
    assert data['list_id'] == list_id
    assert data['completed'] is False

def test_toggle_task(client):
    res_list = client.post('/lists', json={'name': 'Errands'}, headers={'Accept': 'application/json'})
    list_id = res_list.get_json()['id']
    res_task = client.post(f'/lists/{list_id}/tasks', json={'description': 'Run code'}, headers={'Accept': 'application/json'})
    task_id = res_task.get_json()['id']

    # Toggle to complete
    res_toggle = client.post(f'/tasks/{task_id}/toggle', headers={'Accept': 'application/json'})
    assert res_toggle.status_code == 200
    assert res_toggle.get_json()['completed'] is True

    # Toggle back to incomplete
    res_toggle2 = client.post(f'/tasks/{task_id}/toggle', headers={'Accept': 'application/json'})
    assert res_toggle2.get_json()['completed'] is False

def test_delete_task(client):
    res_list = client.post('/lists', json={'name': 'Temp List'}, headers={'Accept': 'application/json'})
    list_id = res_list.get_json()['id']
    res_task = client.post(f'/lists/{list_id}/tasks', json={'description': 'Temp task'}, headers={'Accept': 'application/json'})
    task_id = res_task.get_json()['id']

    res_del = client.post(f'/tasks/{task_id}/delete', headers={'Accept': 'application/json'})
    assert res_del.status_code == 200
    assert task_id not in tasks_db

def test_delete_list_cascade(client):
    res_list = client.post('/lists', json={'name': 'Project X'}, headers={'Accept': 'application/json'})
    list_id = res_list.get_json()['id']
    res_task = client.post(f'/lists/{list_id}/tasks', json={'description': 'Sub task'}, headers={'Accept': 'application/json'})
    task_id = res_task.get_json()['id']

    res_del_list = client.post(f'/lists/{list_id}/delete', headers={'Accept': 'application/json'})
    assert res_del_list.status_code == 200
    assert list_id not in lists_db
    assert task_id not in tasks_db
