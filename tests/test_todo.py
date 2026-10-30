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

def test_task_summary_counts(client):
    # Create a list
    response = client.post('/list', data={'name': 'Work'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Work' in response.data
    assert b'Total: 0, Completed: 0' in response.data

    # Add tasks
    client.post('/list/1/task', data={'description': 'Task 1'}, follow_redirects=True)
    client.post('/list/1/task', data={'description': 'Task 2'}, follow_redirects=True)

    response = client.get('/')
    assert b'Total: 2, Completed: 0' in response.data

    # Complete Task 1 (id=1)
    client.post('/task/1/complete', follow_redirects=True)
    response = client.get('/')
    assert b'Total: 2, Completed: 1' in response.data
