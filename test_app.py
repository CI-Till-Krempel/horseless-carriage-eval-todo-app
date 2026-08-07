import pytest
from app import app, db, TodoList, Task

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do List Application' in response.data

def test_create_list(client):
    response = client.post('/list/create', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_and_toggle_task(client):
    client.post('/list/create', data={'name': 'Work'}, follow_redirects=True)
    response = client.post('/list/1/task/add', data={'description': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data

    # Toggle complete
    response = client.post('/task/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'completed' in response.data or b'Mark Incomplete' in response.data

def test_delete_task(client):
    client.post('/list/create', data={'name': 'Chores'}, follow_redirects=True)
    client.post('/list/1/task/add', data={'description': 'Clean room'}, follow_redirects=True)
    response = client.post('/task/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Clean room' not in response.data

def test_delete_list(client):
    client.post('/list/create', data={'name': 'Temp List'}, follow_redirects=True)
    response = client.post('/list/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temp List' not in response.data
