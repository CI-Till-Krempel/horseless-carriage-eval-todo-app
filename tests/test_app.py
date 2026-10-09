import pytest
from app import app
from models import db, TodoList, Task

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_index_and_create_list(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

    response = client.post('/list/create', data={'name': 'Work Tasks'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Work Tasks' in response.data

def test_add_and_complete_task(client):
    client.post('/list/create', data={'name': 'Groceries'}, follow_redirects=True)
    todo_list = TodoList.query.first()
    
    response = client.post(f'/list/{todo_list.id}/task/add', data={'title': 'Buy Milk'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy Milk' in response.data

    task = Task.query.first()
    assert task.completed is False

    response = client.post(f'/task/{task.id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    task = Task.query.get(task.id)
    assert task.completed is True

def test_delete_task_and_list(client):
    client.post('/list/create', data={'name': 'Temp List'}, follow_redirects=True)
    todo_list = TodoList.query.first()
    client.post(f'/list/{todo_list.id}/task/add', data={'title': 'Temp Task'}, follow_redirects=True)
    
    task = Task.query.first()
    response = client.post(f'/task/{task.id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert Task.query.count() == 0

    response = client.post(f'/list/{todo_list.id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert TodoList.query.count() == 0
