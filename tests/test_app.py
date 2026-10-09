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

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do Lists' in response.data

def test_create_list_and_tasks(client):
    response = client.post('/add_list', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

    # Add task
    response = client.post('/add_task/1', data={'title': 'Buy Milk'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy Milk' in response.data

    # Toggle task
    response = client.post('/toggle_task/1', follow_redirects=True)
    assert response.status_code == 200
    assert b'class="completed"' in response.data or b'Unmark' in response.data

    # Delete task
    response = client.post('/delete_task/1', follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy Milk' not in response.data

    # Delete list
    response = client.post('/delete_list/1', follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' not in response.data
