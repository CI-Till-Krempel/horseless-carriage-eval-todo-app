import pytest
from app import app, lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists.clear()
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data
    assert len(lists) == 1
    assert lists[0]['name'] == 'Groceries'

def test_add_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    response = client.post('/lists/1/tasks', data={'content': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data
    assert len(lists[0]['tasks']) == 1
    assert lists[0]['tasks'][0]['content'] == 'Finish report'

def test_toggle_task(client):
    client.post('/lists', data={'name': 'Home'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'content': 'Clean room'}, follow_redirects=True)
    assert lists[0]['tasks'][0]['completed'] is False
    
    response = client.post('/lists/1/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert lists[0]['tasks'][0]['completed'] is True

def test_delete_task(client):
    client.post('/lists', data={'name': 'Errands'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'content': 'Buy milk'}, follow_redirects=True)
    assert len(lists[0]['tasks']) == 1
    
    response = client.post('/lists/1/tasks/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert len(lists[0]['tasks']) == 0
