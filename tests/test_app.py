import pytest
from app import app, lists_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    lists_db.clear()
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My To-Do Lists' in response.data

def test_create_and_view_list(client):
    response = client.post('/lists', json={"name": "Work Tasks"}, content_type='application/json')
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Work Tasks"

    # Verify listing shows up on index
    res = client.get('/')
    assert b'Work Tasks' in res.data

def test_add_and_toggle_task(client):
    # Create list first
    res = client.post('/lists', json={"name": "Groceries"}, content_type='application/json')
    list_id = res.get_json()["id"]

    # Add task
    t_res = client.post(f'/lists/{list_id}/tasks', json={"text": "Buy Milk"}, content_type='application/json')
    assert t_res.status_code == 201
    task_id = t_res.get_json()["id"]

    # Toggle task
    toggle_res = client.post(f'/tasks/{task_id}/toggle', content_type='application/json')
    assert toggle_res.status_code == 200
    assert toggle_res.get_json()["completed"] is True
