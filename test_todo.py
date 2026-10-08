import os
import tempfile
import pytest
from app import create_app
from models import db, ToDoList, Task

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': f'sqlite:///{db_path}'
    })

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

    os.close(db_fd)
    os.unlink(db_path)

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Work Projects'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Work Projects' in response.data

def test_add_task(client):
    client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    response = client.post('/lists/1/tasks', data={'description': 'Buy milk'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy milk' in response.data

def test_toggle_task(client):
    client.post('/lists', data={'name': 'Chores'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'description': 'Take out trash'}, follow_redirects=True)
    
    # Toggle complete
    response = client.post('/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'completed' in response.data or b'Incomplete' in response.data

def test_delete_task(client):
    client.post('/lists', data={'name': 'Chores'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'description': 'Clean room'}, follow_redirects=True)
    
    response = client.post('/tasks/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Clean room' not in response.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Temporary List'}, follow_redirects=True)
    response = client.post('/lists/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temporary List' not in response.data
