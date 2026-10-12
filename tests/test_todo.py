import pytest
from app import app, lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists.clear()
        # Reset IDs for predictable test IDs
        import app as app_module
        app_module.next_list_id = 1
        app_module.next_task_id = 1
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do List App' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    response = client.post('/lists/1/tasks', data={'content': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data

def test_toggle_task(client):
    client.post('/lists', data={'name': 'Chores'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'content': 'Mow lawn'}, follow_redirects=True)
    
    # Toggle complete
    response = client.post('/lists/1/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'completed' in response.data

def test_delete_task(client):
    client.post('/lists', data={'name': 'Chores'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'content': 'Mow lawn'}, follow_redirects=True)
    
    response = client.post('/lists/1/tasks/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Mow lawn' not in response.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Temp List'}, follow_redirects=True)
    assert b'Temp List' in client.get('/').data
    
    response = client.post('/lists/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temp List' not in response.data
