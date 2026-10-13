import os
import tempfile
import pytest

from app import app, db, TodoList, Task

@pytest.fixture(autouse=True)
def app_context():
    db_fd, db_path = tempfile.mkstemp()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()

    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client():
    return app.test_client()

def test_index_empty(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_us0002_add_task_to_list(client):
    client.post('/lists', data={'name': 'Shopping'}, follow_redirects=True)
    todo_list = TodoList.query.filter_by(name='Shopping').first()
    list_id = todo_list.id

    response = client.post(f'/lists/{list_id}/tasks', data={'description': 'Buy apples'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy apples' in response.data

def test_add_and_complete_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    todo_list = TodoList.query.first()
    list_id = todo_list.id

    client.post(f'/lists/{list_id}/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    task = Task.query.first()
    task_id = task.id

    response = client.post(f'/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200

    response = client.post(f'/tasks/{task_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' not in response.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Temporary List'}, follow_redirects=True)
    todo_list = TodoList.query.first()
    list_id = todo_list.id

    response = client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temporary List' not in response.data
