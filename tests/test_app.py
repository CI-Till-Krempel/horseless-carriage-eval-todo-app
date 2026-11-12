import pytest
from app import app, lists, tasks

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists.clear()
        tasks.clear()
        yield client

def test_toggle_task_complete(client):
    lists['1'] = {'id': '1', 'title': 'Work'}
    tasks['1'] = {'id': '1', 'list_id': '1', 'content': 'Finish report', 'completed': False}

    response = client.post('/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert tasks['1']['completed'] is True

    response = client.post('/tasks/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert tasks['1']['completed'] is False

def test_api_toggle_task(client):
    lists['1'] = {'id': '1', 'title': 'Work'}
    tasks['1'] = {'id': '1', 'list_id': '1', 'content': 'Finish report', 'completed': False}

    response = client.post('/api/tasks/1/toggle')
    assert response.status_code == 200
    data = response.get_json()
    assert data['completed'] is True
