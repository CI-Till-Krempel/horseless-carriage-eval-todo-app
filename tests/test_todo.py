import pytest
from app import app, lists

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        lists.clear()
        yield client

def test_add_task_to_list(client):
    # First create a list
    client.post("/lists", data={"name": "Groceries"})
    # Add a task to list "1"
    response = client.post("/lists/1/tasks", data={"description": "Buy milk"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Buy milk" in response.data
