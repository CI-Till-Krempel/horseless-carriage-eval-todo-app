from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create_list():
    response = client.post("/lists", json={"name": "Groceries"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Groceries"
    assert "id" in data
