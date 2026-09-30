import os
import pytest
from app import app, db, TodoList, Task

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_index_empty(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_and_toggle_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    res = client.post('/lists/1/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    assert b'Finish report' in res.data

    # Toggle complete
    res_toggle = client.post('/tasks/1/toggle', follow_redirects=True)
    assert b'line-through' in res_toggle.data

def test_delete_task(client):
    client.post('/lists', data={'name': 'Home'}, follow_redirects=True)
    client.post('/lists/1/tasks', data={'description': 'Clean room'}, follow_redirects=True)
    res = client.post('/tasks/1/delete', follow_redirects=True)
    assert b'Clean room' not in res.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Temp List'}, follow_redirects=True)
    res = client.post('/lists/1/delete', follow_redirects=True)
    assert b'Temp List' not in res.data
