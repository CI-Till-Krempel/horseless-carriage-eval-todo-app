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

def test_delete_task(client):
    with app.app_context():
        l = TodoList(name="Test List")
        db.session.add(l)
        db.session.commit()
        t = Task(content="Task to Delete", complete=False, list_id=l.id)
        db.session.add(t)
        db.session.commit()
        task_id = t.id

    response = client.post(f'/task/{task_id}/delete', follow_redirects=True)
    assert response.status_code == 200

    with app.app_context():
        deleted_task = Task.query.get(task_id)
        assert deleted_task is None
