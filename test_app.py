import pytest
from app import app, db, TodoList, Task

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        client = app.test_client()
        yield client
        db.drop_all()

def test_index_and_create_list(client):
    response = client.get('/')
    assert response.status_code == 200
    
    response = client.post('/list/add', data={'name': 'My Test List'}, follow_redirects=True)
    assert response.status_code == 200

def test_add_and_toggle_task(client):
    client.post('/list/add', data={'name': 'Task List'}, follow_redirects=True)
    response = client.post('/list/1/task/add', data={'description': 'Write Unit Tests'}, follow_redirects=True)
    assert response.status_code == 200
    
    # Toggle complete
    response = client.post('/task/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    
    # Delete task
    response = client.post('/task/1/delete', follow_redirects=True)
    assert response.status_code == 200

def test_delete_list(client):
    client.post('/list/add', data={'name': 'Obsolete List'}, follow_redirects=True)
    response = client.post('/list/1/delete', follow_redirects=True)
    assert response.status_code == 200
