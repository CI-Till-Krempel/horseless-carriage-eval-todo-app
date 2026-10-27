import os
import tempfile
import pytest

from app import app
import database

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    
    # Override database path for testing
    database.DATABASE = app.config['DATABASE']
    database.init_db()

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'To-Do Lists' in rv.data

def test_create_list(client):
    rv = client.post('/lists', data=dict(name='Groceries'), follow_redirects=True)
    assert rv.status_code == 200
    assert b'Groceries' in rv.data

def test_add_and_complete_task(client):
    client.post('/lists', data=dict(name='Work'), follow_redirects=True)
    db = database.get_db()
    lst = db.execute('SELECT id FROM lists WHERE name = ?', ('Work',)).fetchone()
    list_id = lst['id']
    db.close()

    rv = client.post(f'/lists/{list_id}/tasks', data=dict(description='Finish report'), follow_redirects=True)
    assert rv.status_code == 200
    assert b'Finish report' in rv.data

    db = database.get_db()
    task = db.execute('SELECT id FROM tasks WHERE list_id = ?', (list_id,)).fetchone()
    task_id = task['id']
    db.close()

    rv = client.post(f'/tasks/{task_id}/toggle', follow_redirects=True)
    assert rv.status_code == 200

    rv = client.post(f'/tasks/{task_id}/delete', follow_redirects=True)
    assert rv.status_code == 200
    assert b'Finish report' not in rv.data

    rv = client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert rv.status_code == 200
    assert b'Work' not in rv.data
