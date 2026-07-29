import pytest
from app import app, init_db, DB_NAME
import os

@pytest.fixture
def client():
    app.config['TESTING'] = True
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
    init_db()
    with app.test_client() as client:
        yield client
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_toggle_task_status(client):
    # Create list and task
    client.post('/lists', data={'name': 'Home'})
    client.post('/lists/1/tasks', data={'description': 'Clean room'})

    # Toggle to complete
    client.post('/tasks/1/toggle', follow_redirects=True)
    response = client.get('/')
    assert b'class="task-item completed"' in response.data

    # Toggle back to incomplete
    client.post('/tasks/1/toggle', follow_redirects=True)
    response = client.get('/')
    assert b'class="task-item completed"' not in response.data
    assert b'Clean room' in response.data
