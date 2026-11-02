import pytest
from app import app, lists
import app as app_module

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists.clear()
        app_module.list_counter = 1
        app_module.task_counter = 1
        yield client

def test_create_list(client):
    response = client.post('/lists', data={'title': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_task(client):
    client.post('/lists', data={'title': 'Groceries'}, follow_redirects=True)
    response = client.post('/lists/1/tasks', data={'description': 'Buy milk'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy milk' in response.data
