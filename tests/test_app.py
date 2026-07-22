import os
import pytest
from app import app, init_db, DB_PATH, get_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    test_db = 'test_todo.db'
    if os.path.exists(test_db):
        os.remove(test_db)
    
    import app as app_module
    app_module.DB_PATH = test_db
    app_module.init_db(test_db)
    
    with app.test_client() as client:
        yield client
        
    if os.path.exists(test_db):
        os.remove(test_db)

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Work' in response.data

def test_add_edit_toggle_delete_task(client):
    client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    
    conn = get_db()
    lst = conn.execute('SELECT * FROM lists').fetchone()
    list_id = lst['id']
    conn.close()

    # Add task
    response = client.post(f'/lists/{list_id}/tasks', data={'text': 'Buy milk'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy milk' in response.data
    
    conn = get_db()
    task = conn.execute('SELECT * FROM tasks').fetchone()
    task_id = task['id']
    conn.close()

    # Edit task
    response = client.post(f'/tasks/{task_id}/edit', data={'text': 'Buy organic milk'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy organic milk' in response.data

    # Toggle complete
    response = client.post(f'/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    
    conn = get_db()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    assert task['completed'] == 1
    conn.close()

    # Filter tasks
    response = client.get('/?filter=active')
    assert response.status_code == 200
    assert b'Buy organic milk' not in response.data

    response = client.get('/?filter=completed')
    assert response.status_code == 200
    assert b'Buy organic milk' in response.data

    # Delete task
    response = client.post(f'/tasks/{task_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    
    conn = get_db()
    tasks_count = conn.execute('SELECT COUNT(*) FROM tasks').fetchone()[0]
    conn.close()
    assert tasks_count == 0

def test_delete_list(client):
    client.post('/lists', data={'name': 'Temporary'}, follow_redirects=True)
    conn = get_db()
    list_id = conn.execute('SELECT id FROM lists').fetchone()['id']
    conn.close()
    
    client.post(f'/lists/{list_id}/tasks', data={'text': 'Temp task'}, follow_redirects=True)

    response = client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    
    conn = get_db()
    lists_count = conn.execute('SELECT COUNT(*) FROM lists').fetchone()[0]
    tasks_count = conn.execute('SELECT COUNT(*) FROM tasks').fetchone()[0]
    conn.close()
    assert lists_count == 0
    assert tasks_count == 0
