import os
import tempfile
import pytest
from app import create_app
from models import db, TodoList, Task

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': f'sqlite:///{db_path}',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    })

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_empty(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data
    assert b'No to-do lists found' in response.data

def test_create_list(client):
    response = client.post('/list/create', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_task(client):
    client.post('/list/create', data={'name': 'Work'}, follow_redirects=True)
    response = client.post('/list/1/task/create', data={'title': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data

def test_toggle_task(client):
    client.post('/list/create', data={'name': 'Chores'}, follow_redirects=True)
    client.post('/list/1/task/create', data={'title': 'Clean room'}, follow_redirects=True)
    
    # Toggle complete
    response = client.post('/task/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'class="completed"' in response.data or b'Mark Incomplete' in response.data

    # Toggle incomplete again
    response = client.post('/task/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'Mark Complete' in response.data

def test_delete_task(client):
    client.post('/list/create', data={'name': 'Errands'}, follow_redirects=True)
    client.post('/list/1/task/create', data={'title': 'Buy milk'}, follow_redirects=True)
    
    response = client.post('/task/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy milk' not in response.data

def test_delete_list(client):
    client.post('/list/create', data={'name': 'Temp List'}, follow_redirects=True)
    client.post('/list/1/task/create', data={'title': 'Temp Task'}, follow_redirects=True)
    
    response = client.post('/list/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temp List' not in response.data
    assert b'Temp Task' not in response.data
