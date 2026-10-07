import os
import tempfile
import pytest

from app import app, db, TodoList, Task

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{app.config["DATABASE"]}'
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_index_empty(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_and_complete_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    with app.app_context():
        todo_list = TodoList.query.filter_by(name='Work').first()
        list_id = todo_list.id

    response = client.post(f'/lists/{list_id}/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data

    with app.app_context():
        task = Task.query.filter_by(description='Finish report').first()
        task_id = task.id
        assert task.completed is False

    response = client.post(f'/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200

    with app.app_context():
        task = Task.query.get(task_id)
        assert task.completed is True

def test_delete_task(client):
    client.post('/lists', data={'name': 'Chores'}, follow_redirects=True)
    with app.app_context():
        todo_list = TodoList.query.filter_by(name='Chores').first()
        list_id = todo_list.id

    client.post(f'/lists/{list_id}/tasks', data={'description': 'Clean room'}, follow_redirects=True)
    with app.app_context():
        task = Task.query.filter_by(description='Clean room').first()
        task_id = task.id

    response = client.post(f'/tasks/{task_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Clean room' not in response.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Temp List'}, follow_redirects=True)
    with app.app_context():
        todo_list = TodoList.query.filter_by(name='Temp List').first()
        list_id = todo_list.id

    response = client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temp List' not in response.data
