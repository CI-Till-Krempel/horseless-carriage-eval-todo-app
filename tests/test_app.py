import os
import pytest
from app import app, DATA_FILE

@pytest.fixture
pythontest_client():
    app.config['TESTING'] = True
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    with app.test_client() as client:
        yield client
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

def test_index_empty(pythontest_client):
    response = pythontest_client.get('/')
    assert response.status_code == 200
    assert b'To-Do List Web App' in response.data

def test_create_and_view_list(pythontest_client):
    response = pythontest_client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_and_toggle_task(pythontest_client):
    pythontest_client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    from app import load_data
    data = load_data()
    list_id = data['lists'][0]['id']

    res_task = pythontest_client.post(f'/lists/{list_id}/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    assert b'Finish report' in res_task.data

    data = load_data()
    task_id = data['lists'][0]['tasks'][0]['id']

    res_toggle = pythontest_client.post(f'/lists/{list_id}/tasks/{task_id}/toggle', follow_redirects=True)
    assert res_toggle.status_code == 200

    data = load_data()
    assert data['lists'][0]['tasks'][0]['completed'] is True

def test_delete_task(pythontest_client):
    pythontest_client.post('/lists', data={'name': 'Chores'}, follow_redirects=True)
    from app import load_data
    data = load_data()
    list_id = data['lists'][0]['id']
    pythontest_client.post(f'/lists/{list_id}/tasks', data={'description': 'Sweep floor'}, follow_redirects=True)
    
    data = load_data()
    task_id = data['lists'][0]['tasks'][0]['id']

    res_del = pythontest_client.post(f'/lists/{list_id}/tasks/{task_id}/delete', follow_redirects=True)
    assert b'Sweep floor' not in res_del.data

def test_delete_list(pythontest_client):
    pythontest_client.post('/lists', data={'name': 'Temporary'}, follow_redirects=True)
    from app import load_data
    data = load_data()
    list_id = data['lists'][0]['id']

    res_del = pythontest_client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert b'Temporary' not in res_del.data
