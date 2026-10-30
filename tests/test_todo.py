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

def test_create_list(client):
    response = client.post('/list/create', data={'name': 'Work Tasks'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Work Tasks' in response.data

def test_add_and_toggle_task(client):
    client.post('/list/create', data={'name': 'Groceries'}, follow_redirects=True)
    client.post('/list/1/task/add', data={'description': 'Buy Milk'}, follow_redirects=True)
    response = client.get('/')
    assert b'Buy Milk' in response.data

    # Toggle task complete
    client.post('/task/1/toggle', follow_redirects=True)
    response = client.get('/')
    assert b'completed' in response.data or b'Mark Incomplete' in response.data

def test_delete_task(client):
    client.post('/list/create', data={'name': 'Home'}, follow_redirects=True)
    client.post('/list/1/task/add', data={'description': 'Clean room'}, follow_redirects=True)
    client.post('/task/1/delete', follow_redirects=True)
    response = client.get('/')
    assert b'Clean room' not in response.data

def test_delete_list(client):
    client.post('/list/create', data={'name': 'Temp List'}, follow_redirects=True)
    client.post('/list/1/delete', follow_redirects=True)
    response = client.get('/')
    assert b'Temp List' not in response.data
