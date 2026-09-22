import os
import tempfile
import pytest
from app import app, db, TodoList, Task

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE']
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()

    with app.test_client() as client:
        yield client

    with app.app_context():
        db.drop_all()
    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_index_empty(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b'To-Do List Application' in res.data

def test_create_list(client):
    res = client.post('/list/create', data={'name': 'Groceries'}, follow_redirects=True)
    assert res.status_code == 200
    assert b'Groceries' in res.data

def test_add_and_complete_and_delete_task(client):
    # Create list
    client.post('/list/create', data={'name': 'Work'}, follow_redirects=True)
    with app.app_context():
        todo_list = TodoList.query.first()
        list_id = todo_list.id

    # Add task
    res = client.post(f'/list/{list_id}/task/add', data={'description': 'Write tests'}, follow_redirects=True)
    assert res.status_code == 200
    assert b'Write tests' in res.data

    with app.app_context():
        task = Task.query.first()
        task_id = task.id
        assert task.completed is False

    # Toggle task complete
    res = client.post(f'/task/{task_id}/toggle', follow_redirects=True)
    assert res.status_code == 200
    with app.app_context():
        task = Task.query.get(task_id)
        assert task.completed is True

    # Delete task
    res = client.post(f'/task/{task_id}/delete', follow_redirects=True)
    assert res.status_code == 200
    with app.app_context():
        task = Task.query.get(task_id)
        assert task is None

def test_delete_list_cascade(client):
    client.post('/list/create', data={'name': 'Personal'}, follow_redirects=True)
    with app.app_context():
        todo_list = TodoList.query.first()
        list_id = todo_list.id

    client.post(f'/list/{list_id}/task/add', data={'description': 'Gym'}, follow_redirects=True)
    with app.app_context():
        assert Task.query.count() == 1

    # Delete list
    client.post(f'/list/{list_id}/delete', follow_redirects=True)
    with app.app_context():
        assert TodoList.query.count() == 0
        assert Task.query.count() == 0
