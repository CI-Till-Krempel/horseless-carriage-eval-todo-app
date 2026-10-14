import pytest
from app import app, lists, tasks

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists.clear()
        tasks.clear()
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do List Web Application' in response.data

def test_create_list(client):
    response = client.post('/list/create', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data
    assert 'Groceries' in lists

def test_add_and_toggle_task(client):
    client.post('/list/create', data={'name': 'Work'}, follow_redirects=True)
    client.post('/list/Work/task/add', data={'description': 'Finish report'}, follow_redirects=True)
    assert len(tasks['Work']) == 1
    assert tasks['Work'][0]['description'] == 'Finish report'
    assert not tasks['Work'][0]['completed']

    # Toggle complete
    client.post('/list/Work/task/1/toggle', follow_redirects=True)
    assert tasks['Work'][0]['completed']

def test_delete_task(client):
    client.post('/list/create', data={'name': 'Work'}, follow_redirects=True)
    client.post('/list/Work/task/add', data={'description': 'Temp task'}, follow_redirects=True)
    assert len(tasks['Work']) == 1
    client.post('/list/Work/task/1/delete', follow_redirects=True)
    assert len(tasks['Work']) == 0

def test_delete_list(client):
    client.post('/list/create', data={'name': 'Obsolete'}, follow_redirects=True)
    assert 'Obsolete' in lists
    client.post('/list/Obsolete/delete', follow_redirects=True)
    assert 'Obsolete' not in lists
