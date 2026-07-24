import pytest
from app import app, lists_store


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        lists_store.clear()
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"My To-Do Lists" in response.data


def test_create_list_and_add_task(client):
    # Create list
    response = client.post("/lists", data={"name": "Work Tasks"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Work Tasks" in response.data

    # Find list id from store
    assert len(lists_store) == 1
    list_id = list(lists_store.keys())[0]

    # Add task
    response = client.post(
        f"/lists/{list_id}/tasks", data={"text": "Finish report"}, follow_redirects=True
    )
    assert response.status_code == 200
    assert b"Finish report" in response.data
    assert len(lists_store[list_id]["tasks"]) == 1
    assert lists_store[list_id]["tasks"][0]["text"] == "Finish report"
