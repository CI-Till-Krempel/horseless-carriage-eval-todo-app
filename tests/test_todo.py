import pytest
from app import app, db, TodoList, Task

@pytest.fixture(autouse=True)
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

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
