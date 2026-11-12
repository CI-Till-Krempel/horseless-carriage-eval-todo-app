import pytest
from app import app, todo_lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        todo_lists.clear()
        yield client

def test_create_list(client):
    response = client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data
    assert len(todo_lists) == 1

def test_add_task(client):
    client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    response = client.post('/lists/1/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data
    assert len(todo_lists['1']['tasks']) == 1
    assert todo_lists['1']['tasks'][0]['description'] == 'Finish report'
