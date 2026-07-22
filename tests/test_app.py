import pytest
from app import create_app, db
from models import TodoList, Task

@pytest.fixture
def client():
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
    })
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_index_empty(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_create_list_validation_empty(client):
    response = client.post('/lists', data={'name': ''}, follow_redirects=True)
    assert response.status_code == 200
    assert b'List name cannot be empty.' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data
    assert b'To-do list created successfully!' in response.data

def test_create_task_validation_empty(client):
    client.post('/lists', data={'name': 'Work'})
    response = client.post('/lists/1/tasks', data={'description': ''}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Task description cannot be empty.' in response.data

def test_create_and_complete_task(client):
    client.post('/lists', data={'name': 'Work'})
    response = client.post('/lists/1/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data
    
    response = client.post('/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'completed' in response.data

def test_delete_task(client):
    client.post('/lists', data={'name': 'Work'})
    client.post('/lists/1/tasks', data={'description': 'Temp Task'}, follow_redirects=True)
    
    response = client.post('/tasks/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temp Task' not in response.data

def test_delete_list(client):
    client.post('/lists', data={'name': 'Obsolete List'}, follow_redirects=True)
    response = client.post('/lists/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Obsolete List' not in response.data
