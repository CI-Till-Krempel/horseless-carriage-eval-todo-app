import os
import tempfile
import pytest
from app import app, init_db, DB_NAME

@pytest.fixture(autouse=True)
def client():
    db_fd, db_path = tempfile.mkstemp()
    app.config["TESTING"] = True
    
    global DB_NAME
    original_db = DB_NAME
    DB_NAME = db_path
    app.config["DATABASE"] = db_path
    
    init_db()
    
    with app.test_client() as client:
        yield client
        
    os.close(db_fd)
    try:
        os.unlink(db_path)
    except OSError:
        pass
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
    client.post("/lists", data={"name": "Personal"})
    response = client.post("/lists/1/tasks", data={"description": "Buy groceries"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Buy groceries" in response.data
    
    response = client.post("/tasks/1/toggle", follow_redirects=True)
    assert response.status_code == 200
    
    response = client.post("/tasks/1/delete", follow_redirects=True)
    assert response.status_code == 200
    assert b"Buy groceries" not in response.data

def test_delete_list(client):
    client.post("/lists", data={"name": "Temporary List"})
    response = client.post("/lists/1/delete", follow_redirects=True)
    assert response.status_code == 200
    assert b"Temporary List" not in response.data
