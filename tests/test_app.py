import pytest
from app import app, lists_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists_db.clear()
        global next_list_id, next_task_id
        import app as app_module
        app_module.next_list_id = 1
        app_module.next_task_id = 1
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data

def test_add_task_to_list(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    response = client.post('/lists/1/tasks', data={'text': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data
