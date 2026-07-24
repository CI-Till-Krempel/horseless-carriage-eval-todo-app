import pytest
from app import app, lists_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    lists_db.clear()
    with app.test_client() as client:
        yield client

def test_add_task_to_list_success(client):
    # Create list
    res = client.post('/lists', json={"name": "Project Tasks"}, content_type='application/json')
    list_id = res.get_json()["id"]

    # Add task with valid description
    t_res = client.post(f'/lists/{list_id}/tasks', json={"text": "Write documentation"}, content_type='application/json')
    assert t_res.status_code == 201
    task_data = t_res.get_json()
    assert task_data["text"] == "Write documentation"
    assert task_data["completed"] is False

    # Verify task appears in list GET
    list_res = client.get(f'/lists/{list_id}')
    assert list_res.status_code == 200
    list_json = list_res.get_json()
    assert len(list_json["tasks"]) == 1
    assert list_json["tasks"][0]["text"] == "Write documentation"

def test_add_task_empty_description(client):
    res = client.post('/lists', json={"name": "Groceries"}, content_type='application/json')
    list_id = res.get_json()["id"]

    t_res = client.post(f'/lists/{list_id}/tasks', json={"text": "   "}, content_type='application/json')
    assert t_res.status_code == 400
    assert "error" in t_res.get_json()

def test_add_task_nonexistent_list(client):
    t_res = client.post('/lists/999/tasks', json={"text": "Should fail"}, content_type='application/json')
    assert t_res.status_code == 404
