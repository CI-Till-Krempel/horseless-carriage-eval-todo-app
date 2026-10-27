import pytest
from app import app, lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_toggle_task(client):
    lists.clear()
    client.post('/create_list', data={'title': 'Work'})
    client.post('/add_task/Work', data={'task': 'Finish report'})
    assert lists['Work'][0]['completed'] is False
    
    response = client.post('/toggle_task/Work/0', follow_redirects=True)
    assert response.status_code == 200
    assert lists['Work'][0]['completed'] is True

    response = client.post('/toggle_task/Work/0', follow_redirects=True)
    assert lists['Work'][0]['completed'] is False
