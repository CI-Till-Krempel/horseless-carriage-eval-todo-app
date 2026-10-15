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

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'To-Do List Application' in rv.data

def test_create_list(client):
    rv = client.post('/list', data={'name': 'Groceries'}, follow_redirects=True)
    assert rv.status_code == 200
    assert b'Groceries' in rv.data

def test_add_task(client):
    client.post('/list', data={'name': 'Work'}, follow_redirects=True)
    with app.app_context():
        todo_list = TodoList.query.first()
        list_id = todo_list.id

    rv = client.post(f'/list/{list_id}/task', data={'description': 'Finish report'}, follow_redirects=True)
    assert rv.status_code == 200
    assert b'Finish report' in rv.data

def test_toggle_task(client):
    client.post('/list', data={'name': 'Chores'}, follow_redirects=True)
    with app.app_context():
        todo_list = TodoList.query.first()
        list_id = todo_list.id

    client.post(f'/list/{list_id}/task', data={'description': 'Wash dishes'}, follow_redirects=True)
    with app.app_context():
        task = Task.query.first()
        task_id = task.id
        assert task.complete is False

    rv = client.post(f'/task/{task_id}/toggle', follow_redirects=True)
    assert rv.status_code == 200
    with app.app_context():
        task = Task.query.get(task_id)
        assert task.complete is True

def test_delete_task(client):
    client.post('/list', data={'name': 'Chores'}, follow_redirects=True)
    with app.app_context():
        todo_list = TodoList.query.first()
        list_id = todo_list.id

    client.post(f'/list/{list_id}/task', data={'description': 'Wash dishes'}, follow_redirects=True)
    with app.app_context():
        task = Task.query.first()
        task_id = task.id

    rv = client.post(f'/task/{task_id}/delete', follow_redirects=True)
    assert rv.status_code == 200
    assert b'Wash dishes' not in rv.data

def test_delete_list(client):
    client.post('/list', data={'name': 'Temp List'}, follow_redirects=True)
    with app.app_context():
        todo_list = TodoList.query.first()
        list_id = todo_list.id

    rv = client.post(f'/list/{list_id}/delete', follow_redirects=True)
    assert rv.status_code == 200
    assert b'Temp List' not in rv.data
