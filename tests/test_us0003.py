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

def test_toggle_task(client):
    with app.app_context():
        l = TodoList(title="Test List")
        db.session.add(l)
        db.session.commit()
        t = Task(content="Test Task", complete=False, list_id=l.id)
        db.session.add(t)
        db.session.commit()
        task_id = t.id

    response = client.post(f'/task/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200

    with app.app_context():
        updated_task = Task.query.get(task_id)
        assert updated_task.complete is True
