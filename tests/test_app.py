import os
import tempfile
import pytest

from app import app, db, TodoList, Task

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    with app.app_context():
        db.create_all()
        
    with app.test_client() as client:
        yield client

    with app.app_context():
        db.drop_all()
    os.close(db_fd)
    os.unlink(db_path)

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_create_and_view_list(client):
    response = client.post('/', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200

def test_toggle_task(client):
    client.post('/', data={'name': 'Work'}, follow_redirects=True)
    client.post('/list/1', data={'title': 'Finish Report'}, follow_redirects=True)
    response = client.post('/task/1/toggle', follow_redirects=True)
    assert response.status_code == 200
