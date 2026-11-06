import pytest
from app import app, lists_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists_db.clear()
        yield client

def test_view_lists_and_tasks(client):
    # Create a list
    response = client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Work' in response.data

    # Add a task
    response = client.post('/lists/1/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data
