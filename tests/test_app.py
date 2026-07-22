import pytest
from app import app, load_data, save_data, DATA_FILE
import os

@pytest.fixture
def client():
    app.config["TESTING"] = True
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    with app.test_client() as client:
        yield client
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

def test_persistence_and_filtering(client):
    # Create list
    response = client.post("/list/create", data={"name": "Work"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Work" in response.data

    data = load_data()
    assert len(data) == 1
    list_id = list(data.keys())[0]

    # Add task 1
    client.post(f"/list/{list_id}/task/add", data={"text": "Task Active"}, follow_redirects=True)
    # Add task 2
    client.post(f"/list/{list_id}/task/add", data={"text": "Task Completed"}, follow_redirects=True)

    data = load_data()
    tasks = data[list_id]["tasks"]
    task1_id = tasks[0]["id"]
    task2_id = tasks[1]["id"]

    # Complete task 2
    client.post(f"/list/{list_id}/task/{task2_id}/toggle", follow_redirects=True)

    # Test filter=active
    response = client.get("/?filter=active")
    assert response.status_code == 200
    assert b"Task Active" in response.data
    assert b"Task Completed" not in response.data

    # Test filter=completed
    response = client.get("/?filter=completed")
    assert response.status_code == 200
    assert b"Task Active" not in response.data
    assert b"Task Completed" in response.data
