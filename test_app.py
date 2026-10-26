import pytest
from app import app, lists

@pytest.fixture(autouse=True)
def run_around_tests():
    lists.clear()
    import app as app_module
    app_module.next_list_id = 1
    app_module.next_task_id = 1
    yield

def test_index():
    app.config['TESTING'] = True
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_create_list():
    app.config['TESTING'] = True
    client = app.test_client()
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_task():
    app.config['TESTING'] = True
    client = app.test_client()
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    response = client.post('/lists/1/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data

def test_toggle_task():
    app.config['TESTING'] = True
    client = app.test_client()
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    response = client.post('/lists/1/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'Mark Incomplete' in response.data

def test_delete_task():
    app.config['TESTING'] = True
    client = app.test_client()
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    response = client.post('/lists/1/tasks/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' not in response.data

def test_delete_list():
    app.config['TESTING'] = True
    client = app.test_client()
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    response = client.post('/lists/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Work' not in response.data
