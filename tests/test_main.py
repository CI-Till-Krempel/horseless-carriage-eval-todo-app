import os
import pytest
from fastapi.testclient import TestClient
from app.database import Base, engine, SessionLocal
from app.main import app

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

client = TestClient(app)

def test_dashboard_empty():
    response = client.get("/")
    assert response.status_code == 200
    assert "To-Do List Dashboard" in response.text

def test_create_list_and_task():
    # Create List
    response = client.post("/lists", data={"name": "Groceries"}, follow_redirects=True)
    assert response.status_code == 200
    assert "Groceries" in response.text

    # Add Task to List ID 1
    response = client.post("/lists/1/tasks", data={"description": "Buy Milk"}, follow_redirects=True)
    assert response.status_code == 200
    assert "Buy Milk" in response.text

    # Toggle Task Complete
    response = client.post("/tasks/1/toggle", follow_redirects=True)
    assert response.status_code == 200
    assert "completed" in response.text

    # Delete Task
    response = client.post("/tasks/1/delete", follow_redirects=True)
    assert response.status_code == 200
    assert "Buy Milk" not in response.text

    # Delete List
    response = client.post("/lists/1/delete", follow_redirects=True)
    assert response.status_code == 200
    assert "Groceries" not in response.text
