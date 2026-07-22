import pytest
from app import app, lists_db

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        lists_db.clear()
        yield client

def test_index_empty(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"To-Do List App" in response.data

def test_create_list_and_tasks(client):
    # Create list
    response = client.post("/list/create", data={"name": "Groceries"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Groceries" in response.data

    # Find list id
    list_id = list(lists_db.keys())[0]

    # Add task
    response = client.post(f"/list/{list_id}/task/add", data={"text": "Buy milk"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Buy milk" in response.data

    task_id = lists_db[list_id]["tasks"][0]["id"]

    # Toggle task
    response = client.post(f"/list/{list_id}/task/{task_id}/toggle", follow_redirects=True)
    assert response.status_code == 200
    assert b"completed" in response.data or b"\xe2\x98\x91" in response.data

    # Delete task
    response = client.post(f"/list/{list_id}/task/{task_id}/delete", follow_redirects=True)
    assert response.status_code == 200
    assert b"Buy milk" not in response.data

    # Delete list
    response = client.post(f"/list/{list_id}/delete", follow_redirects=True)
    assert response.status_code == 200
    assert b"Groceries" not in response.data
