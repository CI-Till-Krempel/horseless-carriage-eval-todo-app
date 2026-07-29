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

def test_visual_distinction_completed_tasks(client):
    # Create list
    client.post('/lists', data={'name': 'Personal'})
    # Add task
    client.post('/lists/1/tasks', data={'description': 'Read book'})

    # Toggle task to complete
    client.post('/tasks/1/toggle', follow_redirects=True)

    # Verify visual distinction (.completed class in HTML)
    response = client.get('/')
    assert response.status_code == 200
    assert b'class="task-item completed"' in response.data
    assert b'Read book' in response.data
