import pytest
from app import app, lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        lists.clear()
        yield client

def test_create_list_and_add_task(client):
    # Create list
    response = client.post('/lists', data={'title': 'Work Tasks'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Work Tasks' in response.data
    assert '1' in lists

    # Add task to list
    response = client.post('/lists/1/tasks', data={'description': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data
    assert len(lists['1']['tasks']) == 1
    assert lists['1']['tasks'][0]['description'] == 'Finish report'
