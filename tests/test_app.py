import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'To-Do Lists' in rv.data

def test_create_list(client):
    rv = client.post('/lists', data=dict(name='Groceries'), follow_redirects=True)
    assert rv.status_code == 200
    assert b'Groceries' in rv.data
