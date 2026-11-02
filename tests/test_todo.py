import pytest
from app import app, lists_db, tasks_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    lists_db.clear()
    tasks_db.clear()
    with app.test_client() as client:
        yield client

def test_toggle_task(client):
    lists_db['1'] = {'id': '1', 'title': 'Test List'}
    tasks_db['1'] = {'id': '1', 'list_id': '1', 'content': 'Test Task', 'completed': False}

    response = client.post('/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert tasks_db['1']['completed'] is True

    response = client.post('/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert tasks_db['1']['completed'] is False
