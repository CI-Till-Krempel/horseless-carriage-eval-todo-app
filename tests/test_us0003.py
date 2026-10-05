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

def test_delete_list_with_tasks(client):
    client.post("/lists", data={"name": "Projects"})
    client.post("/lists/1/tasks", data={"description": "Write code"})
    
    res = client.post("/lists/1/delete", follow_redirects=True)
    assert res.status_code == 200
    assert b"Projects" not in res.data
