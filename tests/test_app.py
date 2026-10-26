import pytest
from app import app, lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists.clear()
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'To-Do Lists' in rv.data

def test_create_list(client):
    rv = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert rv.status_code == 200
    assert b'Groceries' in rv.data

def test_add_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    rv = client.post('/lists/1/tasks', data={'title': 'Finish report'}, follow_redirects=True)
    assert rv.status_code == 200
    assert b'Finish report' in rv.data
