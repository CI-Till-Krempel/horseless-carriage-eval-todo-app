import os
import tempfile
import pytest

from app import app, db, TodoList, Task

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{app.config['DATABASE']}"
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_create_and_view_list(client):
    response = client.post('/', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_and_view_tasks(client):
    client.post('/', data={'name': 'Work'}, follow_redirects=True)
    response = client.post('/list/1', data={'title': 'Finish Report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish Report' in response.data

def test_toggle_task(client):
    client.post('/', data={'name': 'Work'}, follow_redirects=True)
    client.post('/list/1', data={'title': 'Finish Report'}, follow_redirects=True)
    
    # Toggle complete
    response = client.post('/task/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'class="completed"' in response.data or b'Mark Incomplete' in response.data

    # Toggle incomplete
    response = client.post('/task/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'Mark Complete' in response.data

def test_delete_task(client):
    client.post('/', data={'name': 'Work'}, follow_redirects=True)
    client.post('/list/1', data={'title': 'Finish Report'}, follow_redirects=True)
    
    response = client.post('/task/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish Report' not in response.data

def test_delete_list(client):
    client.post('/', data={'name': 'Work'}, follow_redirects=True)
    response = client.post('/list/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Work' not in response.data
