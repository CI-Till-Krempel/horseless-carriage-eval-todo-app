import os
import tempfile
import pytest
from app import app, init_db, DB_NAME

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app.config['TESTING'] = True
    
    global DB_NAME
    original_db = DB_NAME
    DB_NAME = db_path
    init_db()

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    try:
        os.unlink(db_path)
    except Exception:
        pass
    DB_NAME = original_db

def test_index(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b'My To-Do Lists' in res.data

def test_create_and_delete_list(client):
    res = client.post('/add_list', data={'name': 'Work'}, follow_redirects=True)
    assert res.status_code == 200
    assert b'Work' in res.data

    # Delete list (list id starts at 1)
    res = client.post('/delete_list/1', follow_redirects=True)
    assert res.status_code == 200
    assert b'Work' not in res.data

def test_task_lifecycle(client):
    client.post('/add_list', data={'name': 'Groceries'}, follow_redirects=True)
    
    # Add task (list id 1)
    res = client.post('/add_task/1', data={'description': 'Buy milk'}, follow_redirects=True)
    assert res.status_code == 200
    assert b'Buy milk' in res.data

    # Toggle complete (task id 1)
    res = client.post('/toggle_task/1', follow_redirects=True)
    assert res.status_code == 200
    assert b'Undo' in res.data

    # Delete task (task id 1)
    res = client.post('/delete_task/1', follow_redirects=True)
    assert res.status_code == 200
    assert b'Buy milk' not in res.data
