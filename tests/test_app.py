import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

import pytest
from app import app, lists

@pytest.fixture(autouse=True)
def clean_lists():
    lists.clear()
    yield

def test_index_empty():
    app.config['TESTING'] = True
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_create_list():
    app.config['TESTING'] = True
    client = app.test_client()
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_task_and_view():
    app.config['TESTING'] = True
    client = app.test_client()
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    response = client.post('/lists/1/tasks', data={'text': 'Write unit tests'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Write unit tests' in response.data

def test_toggle_and_delete_task():
    app.config['TESTING'] = True
    client = app.test_client()
    client.post('/lists', data={'name': 'Personal'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'text': 'Buy milk'}, follow_redirects=True)
    
    response = client.post('/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'completed' in response.data or b'class="completed"' in response.data

    response = client.post('/tasks/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy milk' not in response.data

def test_delete_list():
    app.config['TESTING'] = True
    client = app.test_client()
    client.post('/lists', data={'name': 'Temp List'}, follow_redirects=True)
    response = client.post('/lists/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temp List' not in response.data
