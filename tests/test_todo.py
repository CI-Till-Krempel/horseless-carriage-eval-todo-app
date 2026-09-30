import os
import tempfile
import pytest
from app import create_app
from models import db, ToDoList, Task

def test_index_route():
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

def test_create_list_route():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({
        'SQLALCHEMY_DATABASE_URI': f'sqlite:///{db_path}',
        'TESTING': True
    })
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        response = client.post('/list/create', data={'name': 'Test List'}, follow_redirects=True)
        assert response.status_code == 200
    os.close(db_fd)
    os.unlink(db_path)
