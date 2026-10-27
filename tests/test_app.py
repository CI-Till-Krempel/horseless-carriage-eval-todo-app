import pytest
from app import app, lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_view_all_lists_and_tasks(client):
    lists.clear()
    lists.append({
        'name': 'Work List',
        'tasks': [
            {'title': 'Finish Report', 'completed': True},
            {'title': 'Email Boss', 'completed': False}
        ]
    })
    response = client.get('/')
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'Work List' in html
    assert 'Finish Report' in html
    assert 'Email Boss' in html
    assert 'text-decoration: line-through' in html
