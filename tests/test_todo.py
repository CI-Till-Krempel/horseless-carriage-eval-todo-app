import os
import tempfile
import pytest

from app import app, db, TodoList, Task

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{app.config["DATABASE"]}'
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_add_task_to_list(client):
    # First create a list
    client.post('/lists', data={'name': 'Work Tasks'}, follow_redirects=True)
    
    with app.app_context():
        todo_list = TodoList.query.first()
        list_id = todo_list.id

    # Now add a task to that list
    response = client.post(f'/lists/{list_id}/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Work Tasks' in response.data
    assert b'Finish report' in response.data

    with app.app_context():
        task = Task.query.first()
        assert task is not None
        assert task.description == 'Finish report'
        assert task.list_id == list_id
