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

def test_delete_list_cascade(client):
    # Create list
    response = client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Work' in response.data

    # Add tasks to list
    client.post('/lists/1/tasks', data={'description': 'Finish report'})
    client.post('/lists/1/tasks', data={'description': 'Send email'})

    # Verify tasks appear
    response = client.get('/')
    assert b'Finish report' in response.data
    assert b'Send email' in response.data

    # Delete entire list (US-0005 verification)
    response = client.post('/lists/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Work' not in response.data
    assert b'Finish report' not in response.data
    assert b'Send email' not in response.data
