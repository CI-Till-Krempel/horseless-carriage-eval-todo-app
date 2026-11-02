import pytest
from app import app, lists, tasks

@pytest.fixture(autouse=True)
def clear_state():
    lists.clear()
    tasks.clear()
    yield

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_list_and_add_task_api(client):
    # Create list via API
    res = client.post('/api/lists', json={'name': 'Groceries'})
    assert res.status_code == 201
    data = res.get_json()
    list_id = data['id']
    assert data['name'] == 'Groceries'

    # Add task via API
    res_task = client.post(f'/api/lists/{list_id}/tasks', json={'content': 'Buy milk'})
    assert res_task.status_code == 201
    task_data = res_task.get_json()
    assert task_data['content'] == 'Buy milk'
    assert task_data['list_id'] == list_id

    # Verify task appears in list tasks
    res_get = client.get(f'/api/lists/{list_id}/tasks')
    assert res_get.status_code == 200
    get_data = res_get.get_json()
    assert len(get_data) == 1
    assert get_data[0]['content'] == 'Buy milk'

def test_add_task_form(client):
    client.post('/lists', data={'name': 'Work'})
    res = client.post('/lists/1/tasks', data={'content': 'Finish report'}, follow_redirects=True)
    assert res.status_code == 200
    assert b'Finish report' in res.data
