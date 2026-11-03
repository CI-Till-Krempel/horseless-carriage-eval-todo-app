import pytest
from app import app, db, TodoList, Task

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_add_list(client):
    response = client.post('/list', data={'title': 'New List'}, follow_redirects=True)
    assert response.status_code == 200
    with app.app_context():
        l = TodoList.query.first()
        assert l is not None
        assert l.name == 'New List'

def test_add_task_to_list(client):
    client.post('/list', data={'title': 'New List'}, follow_redirects=True)
    with app.app_context():
        todo_list = TodoList.query.first()
        list_id = todo_list.id
    response = client.post(f'/list/{list_id}/task', data={'content': 'New Task'}, follow_redirects=True)
    assert response.status_code == 200
    with app.app_context():
        task = Task.query.first()
        assert task is not None
        assert task.content == 'New Task'
        assert task.list_id == list_id
