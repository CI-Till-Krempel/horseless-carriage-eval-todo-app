import pytest
from app import create_app

def test_direct_smoke():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})
    assert app.test_client().get('/').status_code == 200
