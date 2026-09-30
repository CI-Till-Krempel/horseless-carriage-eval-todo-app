import os
import tempfile
import pytest
from app import create_app
from models import db, ToDoList, Task

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({
        'SQLALCHEMY_DATABASE_URI': f'sqlite:///{db_path}',
        'TESTING': True
    })

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

    os.close(db_fd)
    os.unlink(db_path)

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/list/create', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_task(client):
    client.post('/list/create', data={'name': 'Work'}, follow_redirects=True)
    response = client.post('/list/1/task/add', data={'description': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data

def test_toggle_task(client):
    client.post('/list/create', data={'name': 'Work'}, follow_redirects=True)
    client.post('/list/1/task/add', data={'description': 'Finish report'}, follow_redirects=True)
    
    # Toggle complete
    response = client.post('/task/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'completed' in response.data or b'Mark Incomplete' in response.data

    # Toggle back incomplete
    response = client.post('/task/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'Mark Complete' in response.data

def test_delete_task(client):
    client.post('/list/create', data={'name': 'Work'}, follow_redirects=True)
    client.post('/list/1/task/add', data={'description': 'Finish report'}, follow_redirects=True)
    
    response = client.post('/task/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' not in response.data

def test_delete_list(client):
    client.post('/list/create', data={'name': 'Obsolete List'}, follow_redirects=True)
    response = client.post('/list/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Obsolete List' not in response.data
