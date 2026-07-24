import pytest
from app import app, lists_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    lists_db.clear()
    with app.test_client() as client:
        yield client

def test_toggle_task_completion(client):
    # Create list
    res = client.post('/lists', json={"name": "Work"}, content_type='application/json')
    list_id = res.get_json()["id"]

    # Add task
    t_res = client.post(f'/lists/{list_id}/tasks', json={"text": "Review PR"}, content_type='application/json')
    task_id = t_res.get_json()["id"]

    # Toggle complete
    toggle_res = client.post(f'/tasks/{task_id}/toggle', content_type='application/json')
    assert toggle_res.status_code == 200
    assert toggle_res.get_json()["completed"] is True

    # Toggle back to incomplete
    toggle_res_2 = client.post(f'/tasks/{task_id}/toggle', content_type='application/json')
    assert toggle_res_2.status_code == 200
    assert toggle_res_2.get_json()["completed"] is False
