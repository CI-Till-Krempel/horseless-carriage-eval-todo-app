import pytest
from todo_app.app import create_app

def test_smoke():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})
    client = app.test_client()
    assert client.get('/').status_code == 200
