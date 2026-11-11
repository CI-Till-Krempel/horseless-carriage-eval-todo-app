import pytest
from app import app, lists_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    lists_db.clear()
    with app.test_client() as client:
        yield client

def test_delete_task(client):
    client.post('/lists', data={'list_name': 'Work'})
    client.post('/lists/1/tasks', data={'task_title': 'Finish report'})
    assert len(lists_db['1']['tasks']) == 1
    client.post('/lists/1/tasks/1/delete')
    assert len(lists_db['1']['tasks']) == 0
