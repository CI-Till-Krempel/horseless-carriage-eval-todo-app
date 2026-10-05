import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import pytest
from app import create_app
from models import db, TodoList, Task

def test_app_smoke():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200

def test_crud_flow():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})
    client = app.test_client()
    
    # Create list
    res = client.post('/list/create', data={'name': 'My List'}, follow_redirects=True)
    assert res.status_code == 200
    assert b'My List' in res.data
    
    # Add task
    res = client.post('/list/1/task/create', data={'title': 'Task 1'}, follow_redirects=True)
    assert res.status_code == 200
    assert b'Task 1' in res.data
    
    # Toggle task
    res = client.post('/task/1/toggle', follow_redirects=True)
    assert res.status_code == 200
    
    # Delete task
    res = client.post('/task/1/delete', follow_redirects=True)
    assert res.status_code == 200
    assert b'Task 1' not in res.data
    
    # Delete list
    res = client.post('/list/1/delete', follow_redirects=True)
    assert res.status_code == 200
    assert b'My List' not in res.data
