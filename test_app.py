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

def test_add_task_to_list(client):
    # First create a list
    client.post('/add_list', data={'title': 'Work List'}, follow_redirects=True)
    with app.app_context():
        lst = TodoList.query.first()
        list_id = lst.id

    # Now add a task to that list
    response = client.post(f'/add_task/{list_id}', data={'description': 'Write unit tests'}, follow_redirects=True)
    assert response.status_code == 200
    
    with app.app_context():
        task = Task.query.first()
        assert task is not None
        assert task.description == 'Write unit tests'
        assert task.todolist_id == list_id
