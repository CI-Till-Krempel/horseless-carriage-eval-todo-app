import pytest
from app import app, db, TodoList, Task

@pytest.fixture(autouse=True)
def setup_teardown():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield
        db.drop_all()

@pytest.fixture
def client():
    return app.test_client()

def test_create_and_get_list(client):
    response = client.post('/list', data={'title': 'My Tasks'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'My Tasks' in response.data

def test_add_task(client):
    client.post('/list', data={'title': 'Work List'})
    response = client.post('/list/1/task', data={'title': 'Write docs'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Write docs' in response.data

def test_toggle_task(client):
    client.post('/list', data={'title': 'Work List'})
    client.post('/list/1/task', data={'title': 'Finish report'})
    
    # Check task is not completed initially
    with app.app_context():
        task = Task.query.first()
        assert task.completed is False

    # Toggle task to complete
    response = client.post('/task/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    with app.app_context():
        task = Task.query.first()
        assert task.completed is True

    # Toggle task back to incomplete
    response = client.post('/task/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    with app.app_context():
        task = Task.query.first()
        assert task.completed is False
