import os
import tempfile
import pytest

from app import app, db, TodoList, Task

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()

    with app.test_client() as client:
        yield client

    with app.app_context():
        db.drop_all()
    os.close(db_fd)
    os.unlink(db_path)

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_and_toggle_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    with app.app_context():
        todo_list = TodoList.query.first()
        list_id = todo_list.id

    response = client.post(f'/lists/{list_id}/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data

    with app.app_context():
        task = Task.query.first()
        task_id = task.id

    response = client.post(f'/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    
    response = client.post(f'/tasks/{task_id}/delete', follow_redirects=True)
    assert response.status_code == 200

def test_delete_list(client):
    client.post('/lists', data={'name': 'Temp List'}, follow_redirects=True)
    with app.app_context():
        todo_list = TodoList.query.first()
        list_id = todo_list.id

    response = client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temp List' not in response.data
