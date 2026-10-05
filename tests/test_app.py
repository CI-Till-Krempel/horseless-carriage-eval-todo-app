import os
import tempfile
import pytest
from app import app, init_db, DB_NAME, get_db

@pytest.fixture
def client():
    db_fd, app.config["DATABASE"] = tempfile.mkstemp()
    app.config["TESTING"] = True
    
    # Use temporary database
    global DB_NAME
    original_db = DB_NAME
    DB_NAME = app.config["DATABASE"]
    
    init_db()
    
    with app.test_client() as client:
        yield client
        
    os.close(db_fd)
    os.unlink(app.config["DATABASE"])
    DB_NAME = original_db

def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"To-Do List App" in response.data

def test_create_and_view_list(client):
    response = client.post("/lists", data={"name": "Work Tasks"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Work Tasks" in response.data

def test_task_management(client):
    # Create list
    client.post("/lists", data={"name": "Personal"})
    
    # Add task
    response = client.post("/lists/1/tasks", data={"description": "Buy groceries"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Buy groceries" in response.data
    
    # Toggle complete
    response = client.post("/tasks/1/toggle", follow_redirects=True)
    assert response.status_code == 200
    assert b"Mark Incomplete" in response.data or b"completed" in response.data
    
    # Delete task
    response = client.post("/tasks/1/delete", follow_redirects=True)
    assert response.status_code == 200
    assert b"Buy groceries" not in response.data

def test_delete_list(client):
    client.post("/lists", data={"name": "Temporary List"})
    response = client.post("/lists/1/delete", follow_redirects=True)
    assert response.status_code == 200
    assert b"Temporary List" not in response.data
