import os
import tempfile
import pytest
from app import app, init_db, DB_NAME

@pytest.fixture
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

def test_task_management_lifecycle(client):
    client.post("/lists", data={"name": "Groceries"})
    # Add task
    res = client.post("/lists/1/tasks", data={"description": "Buy milk"}, follow_redirects=True)
    assert res.status_code == 200
    assert b"Buy milk" in res.data
    
    # Toggle complete
    res = client.post("/tasks/1/toggle", follow_redirects=True)
    assert res.status_code == 200
    
    # Delete task
    res = client.post("/tasks/1/delete", follow_redirects=True)
    assert res.status_code == 200
    assert b"Buy milk" not in res.data
