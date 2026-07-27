import os
import pytest
from app import app, DATA_FILE, save_data, load_data

@pytest.fixture
def client():
    app.config['TESTING'] = True
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    with app.test_client() as client:
        yield client
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_help_page(client):
    response = client.get('/help')
    assert response.status_code == 200
    assert b'User Guide & Help' in response.data

def test_persistence_flow(client):
    # 1. Create list
    response = client.post('/lists', data={'name': 'Persistent List'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Persistent List' in response.data

    # Verify JSON file exists and contains data
    assert os.path.exists(DATA_FILE)
    data = load_data()
    assert len(data['lists']) == 1
    list_id = list(data['lists'].keys())[0]

    # 2. Add task
    response = client.post(f'/lists/{list_id}/tasks', data={'title': 'Persistent Task'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Persistent Task' in response.data

    data = load_data()
    assert len(data['lists'][list_id]['tasks']) == 1
    task_id = list(data['lists'][list_id]['tasks'].keys())[0]

    # 3. Toggle task
    client.post(f'/lists/{list_id}/tasks/{task_id}/toggle', follow_redirects=True)
    data = load_data()
    assert data['lists'][list_id]['tasks'][task_id]['completed'] is True

    # 4. Delete task
    client.post(f'/lists/{list_id}/tasks/{task_id}/delete', follow_redirects=True)
    data = load_data()
    assert len(data['lists'][list_id]['tasks']) == 0

    # 5. Delete list
    client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    data = load_data()
    assert len(data['lists']) == 0
