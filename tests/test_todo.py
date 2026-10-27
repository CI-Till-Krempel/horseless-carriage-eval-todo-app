import pytest
from app import app, lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_delete_task(client):
    lists.clear()
    client.post('/create_list', data={'title': 'Work'})
    client.post('/add_task/Work', data={'task': 'Finish report'})
    assert len(lists['Work']) == 1
    
    response = client.post('/delete_task/Work/0', follow_redirects=True)
    assert response.status_code == 200
    assert len(lists['Work']) == 0
