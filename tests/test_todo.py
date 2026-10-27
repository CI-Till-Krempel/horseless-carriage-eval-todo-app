import pytest
from app import app, lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_delete_list(client):
    lists.clear()
    client.post('/create_list', data={'title': 'Work'})
    client.post('/add_task/Work', data={'task': 'Finish report'})
    assert 'Work' in lists
    assert len(lists['Work']) == 1
    
    response = client.post('/delete_list/Work', follow_redirects=True)
    assert response.status_code == 200
    assert 'Work' not in lists
