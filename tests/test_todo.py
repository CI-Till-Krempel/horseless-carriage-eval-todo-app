import os
import pytest
from app import app, db, TodoList, Task

@pytest.fixture
pythontest_client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_index_route(pythontest_client):
    response = pythontest_client.get('/')
    assert response.status_code == 200

def test_create_list(pythontest_client):
    response = pythontest_client.post('/lists', data={'name': 'Work Tasks'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Work Tasks' in response.data

def test_add_task(pythontest_client):
    pythontest_client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    with app.app_context():
        lst = TodoList.query.first()
        list_id = lst.id
    response = pythontest_client.post(f'/lists/{list_id}/tasks', data={'description': 'Buy Milk'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy Milk' in response.data

def test_toggle_task(pythontest_client):
    pythontest_client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    with app.app_context():
        lst = TodoList.query.first()
        list_id = lst.id
    pythontest_client.post(f'/lists/{list_id}/tasks', data={'description': 'Buy Milk'}, follow_redirects=True)
    with app.app_context():
        task = Task.query.first()
        task_id = task.id
    response = pythontest_client.post(f'/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'completed' in response.data

def test_delete_task(pythontest_client):
    pythontest_client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    with app.app_context():
        lst = TodoList.query.first()
        list_id = lst.id
    pythontest_client.post(f'/lists/{list_id}/tasks', data={'description': 'Buy Milk'}, follow_redirects=True)
    with app.app_context():
        task = Task.query.first()
        task_id = task.id
    response = pythontest_client.post(f'/tasks/{task_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy Milk' not in response.data

def test_delete_list(pythontest_client):
    pythontest_client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    with app.app_context():
        lst = TodoList.query.first()
        list_id = lst.id
    response = pythontest_client.post(f'/lists/{list_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' not in response.data
