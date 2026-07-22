import os
import pytest
from fastapi.testclient import TestClient
from app.database import Base, engine, SessionLocal, TodoList, Task
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
    response = client.post("/lists", data={"name": "Groceries"}, follow_redirects=True)
    assert response.status_code == 200
    assert "Groceries" in response.text

    response = client.post("/lists/1/tasks", data={"description": "Buy Milk"}, follow_redirects=True)
    assert response.status_code == 200
    assert "Buy Milk" in response.text

def test_task_completion_toggle():
    client.post("/lists", data={"name": "Home"}, follow_redirects=True)
    client.post("/lists/1/tasks", data={"description": "Clean Room"}, follow_redirects=True)
    
    # Toggle complete
    response = client.post("/tasks/1/toggle", follow_redirects=True)
    assert response.status_code == 200
    assert "Mark Incomplete" in response.text

    # Toggle incomplete
    response = client.post("/tasks/1/toggle", follow_redirects=True)
    assert response.status_code == 200
    assert "Mark Complete" in response.text

def test_task_deletion():
    client.post("/lists", data={"name": "Errands"}, follow_redirects=True)
    client.post("/lists/1/tasks", data={"description": "Post Letter"}, follow_redirects=True)
    assert "Post Letter" in client.get("/").text

    response = client.post("/tasks/1/delete", follow_redirects=True)
    assert response.status_code == 200
    assert "Post Letter" not in response.text

def test_delete_list_cascade(():
    client.post("/lists", data={"name": "Project X"}, follow_redirects=True)
    client.post("/lists/1/tasks", data={"description": "Task 1"}, follow_redirects=True)
    client.post("/lists/1/tasks", data={"description": "Task 2"}, follow_redirects=True)
    
    html = client.get("/").text
    assert "Project X" in html
    assert "Task 1" in html
    assert "Task 2" in html

    # Delete list (US-0005)
    response = client.post("/lists/1/delete", follow_redirects=True)
    assert response.status_code == 200
    
    html_after = client.get("/").text
    assert "Project X" not in html_after
    assert "Task 1" not in html_after
    assert "Task 2" not in html_after

def test_nonexistent_endpoints():
    assert client.post("/tasks/999/toggle").status_code == 404
    assert client.post("/tasks/999/delete").status_code == 404
    assert client.post("/lists/999/delete").status_code == 404
    assert client.post("/lists/999/tasks", data={"description": "fail"}).status_code == 404
