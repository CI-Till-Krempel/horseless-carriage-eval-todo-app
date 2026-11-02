import pytest
from app import app, lists, tasks

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists.clear()
        tasks.clear()
        yield client

def test_toggle_task(client):
    lists['list_1'] = {'id': 'list_1', 'name': 'Work'}
    tasks['task_1'] = {'id': 'task_1', 'list_id': 'list_1', 'title': 'Test Task', 'completed': False}
    
    response = client.post('/task/task_1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert tasks['task_1']['completed'] is True

    response = client.post('/task/task_1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert tasks['task_1']['completed'] is False
