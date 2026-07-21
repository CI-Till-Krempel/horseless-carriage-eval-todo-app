import pytest
from app import app, lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'My To-Do Lists' in rv.data

def test_create_list(client):
    rv = client.post('/', data={'list_name': 'Test List'}, follow_redirects=True)
    assert rv.status_code == 200
    assert b'Test List' in rv.data

def test_add_task(client):
    # First create a list
    client.post('/', data={'list_name': 'Test List'}, follow_redirects=True)
    list_id = list(lists.keys())[0]
    
    rv = client.post(f'/add_task/{list_id}', data={'task_text': 'New Task'}, follow_redirects=True)
    assert rv.status_code == 200
    assert b'New Task' in rv.data
