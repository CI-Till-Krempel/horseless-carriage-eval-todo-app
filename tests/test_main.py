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
    response = client.post("/lists", data={"name": "Work Tasks"}, follow_redirects=True)
    assert response.status_code == 200
    assert "Work Tasks" in response.text

    # Add Task to List ID 1
    response = client.post("/lists/1/tasks", data={"description": "Finish Report"}, follow_redirects=True)
    assert response.status_code == 200
    assert "Finish Report" in response.text

def test_task_completion_toggle():
    client.post("/lists", data={"name": "Personal"}, follow_redirects=True)
    client.post("/lists/1/tasks", data={"description": "Gym"}, follow_redirects=True)
    
    # Toggle complete (US-0003)
    response = client.post("/tasks/1/toggle", follow_redirects=True)
    assert response.status_code == 200
    assert "Mark Incomplete" in response.text
    assert "completed" in response.text

    # Toggle back to incomplete
    response = client.post("/tasks/1/toggle", follow_redirects=True)
    assert response.status_code == 200
    assert "Mark Complete" in response.text

def test_task_deletion():
    client.post("/lists", data={"name": "Temp List"}, follow_redirects=True)
    client.post("/lists/1/tasks", data={"description": "Task to Delete"}, follow_redirects=True)
    assert "Task to Delete" in client.get("/").text

    # Delete task (US-0004)
    response = client.post("/tasks/1/delete", follow_redirects=True)
    assert response.status_code == 200
    assert "Task to Delete" not in response.text

def test_nonexistent_task_errors():
    response = client.post("/tasks/999/toggle")
    assert response.status_code == 404

    response = client.post("/tasks/999/delete")
    assert response.status_code == 404
