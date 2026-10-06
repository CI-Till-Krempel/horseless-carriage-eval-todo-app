import pytest
from app import app, lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    lists.clear()
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_create_list(client):
    client.post('/lists', data={'name': 'List1'}, follow_redirects=True)
    assert len(lists) == 1

def test_add_and_toggle_task(client):
    client.post('/lists', data={'name': 'List1'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'description': 'Task1'}, follow_redirects=True)
    assert len(lists[0]['tasks']) == 1
    client.post('/lists/1/tasks/1/toggle', follow_redirects=True)
    assert lists[0]['tasks'][0]['completed'] is True

def test_delete_task(client):
    client.post('/lists', data={'name': 'List1'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'description': 'Task1'}, follow_redirects=True)
    client.post('/lists/1/tasks/1/delete', follow_redirects=True)
    assert len(lists[0]['tasks']) == 0

def test_delete_list(client):
    client.post('/lists', data={'name': 'List1'}, follow_redirects=True)
    client.post('/lists/1/delete', follow_redirects=True)
    assert len(lists) == 0
