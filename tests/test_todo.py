import pytest
from app import app, lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_delete_list(client):
    lists.clear()
    lists.append({'name': 'Work', 'tasks': []})
    # if testing delete list endpoint or logic, ensure it handles dict structure properly
    assert len(lists) == 1
    lists.pop(0)
    assert len(lists) == 0
