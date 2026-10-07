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

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Work Tasks'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Work Tasks' in response.data

def test_add_task(client):
    client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    with app.app_context():
        lst = TodoList.query.first()
        list_id = lst.id
    response = client.post(f'/lists/{list_id}/tasks', data={'description': 'Buy Milk'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy Milk' in response.data

def test_toggle_task(client):
    client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    with app.app_context():
        lst = TodoList.query.first()
        list_id = lst.id
    client.post(f'/lists/{list_id}/tasks', data={'description': 'Buy Milk'}, follow_redirects=True)
    with app.app_context():
        task = Task.query.first()
        task_id = task.id
    response = client.post(f'/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'completed' in response.data

def test_delete_task(client):
    client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    with app.app_context():
        lst = TodoList.query.first()
        list_id = lst.id
    client.post(f'/lists/{list_id}/tasks', data={'description': 'Buy Milk'}, follow_redirects=True)
    with app.app_context():
        task = Task.query.first()
        task_id = task.id
    response = client.post(f'/tasks/{task_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy Milk' not in response.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    with app.app_context():
        lst = TodoList.query.first()
        list_id = lst.id
    response = client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' not in response.data
