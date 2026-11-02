import pytest
from app import app, lists_db, tasks_db

@pytest.fixture(autouse=True)
def run_around_tests():
    lists_db.clear()
    tasks_db.clear()
    yield

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_list(client):
    response = client.post('/lists', data={'title': 'My List'}, follow_redirects=True)
    assert response.status_code == 200
    assert len(lists_db) == 1
    assert list(lists_db.values())[0]['title'] == 'My List'

def test_add_task(client):
    lists_db['1'] = {'id': '1', 'title': 'My List'}
    response = client.post('/lists/1/tasks', data={'content': 'Buy milk'}, follow_redirects=True)
    assert response.status_code == 200
    assert len(tasks_db) == 1
    assert list(tasks_db.values())[0]['content'] == 'Buy milk'

def test_toggle_task(client):
    lists_db['1'] = {'id': '1', 'title': 'Test List'}
    tasks_db['1'] = {'id': '1', 'list_id': '1', 'content': 'Test Task', 'completed': False}

    response = client.post('/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert tasks_db['1']['completed'] is True

def test_delete_task(client):
    lists_db['1'] = {'id': '1', 'title': 'Test List'}
    tasks_db['1'] = {'id': '1', 'list_id': '1', 'content': 'Test Task', 'completed': False}

    response = client.post('/tasks/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert len(tasks_db) == 0

def test_delete_list(client):
    lists_db['1'] = {'id': '1', 'title': 'Test List'}
    tasks_db['1'] = {'id': '1', 'list_id': '1', 'content': 'Test Task', 'completed': False}

    response = client.post('/lists/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert len(lists_db) == 0
    assert len(tasks_db) == 0
