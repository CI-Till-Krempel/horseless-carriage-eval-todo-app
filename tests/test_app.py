import pytest
from app import app, todo_lists

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        todo_lists.clear()
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do Lists' in response.data

def test_create_list(client):
    response = client.post('/lists', data={'list_name': 'Groceries'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Groceries' in response.data
    assert 'Groceries' in todo_lists

def test_add_task(client):
    client.post('/lists', data={'list_name': 'Work'}, follow_redirects=True)
    response = client.post('/lists/Work/tasks', data={'task_description': 'Finish report'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Finish report' in response.data
    assert len(todo_lists['Work']) == 1
    assert todo_lists['Work'][0]['description'] == 'Finish report'

def test_toggle_task(client):
    client.post('/lists', data={'list_name': 'Chores'}, follow_redirects=True)
    client.post('/lists/Chores/tasks', data={'task_description': 'Buy milk'}, follow_redirects=True)
    assert todo_lists['Chores'][0]['completed'] is False

    response = client.post('/lists/Chores/tasks/0/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert todo_lists['Chores'][0]['completed'] is True

def test_delete_task(client):
    client.post('/lists', data={'list_name': 'Personal'}, follow_redirects=True)
    client.post('/lists/Personal/tasks', data={'task_description': 'Gym'}, follow_redirects=True)
    assert len(todo_lists['Personal']) == 1

    response = client.post('/lists/Personal/tasks/0/delete', follow_redirects=True)
    assert response.status_code == 200
    assert len(todo_lists['Personal']) == 0
    assert b'Gym' not in response.data

def test_delete_entire_list(client):
    client.post('/lists', data={'list_name': 'Temporary'}, follow_redirects=True)
    client.post('/lists/Temporary/tasks', data={'task_description': 'Temp task'}, follow_redirects=True)
    assert 'Temporary' in todo_lists

    response = client.post('/lists/Temporary/delete', follow_redirects=True)
    assert response.status_code == 200
    assert 'Temporary' not in todo_lists
    assert b'Temporary' not in response.data

def test_view_all_lists_and_tasks(client):
    client.post('/lists', data={'list_name': 'ListA'}, follow_redirects=True)
    client.post('/lists/ListA/tasks', data={'task_description': 'TaskA1'}, follow_redirects=True)
    client.post('/lists', data={'list_name': 'ListB'}, follow_redirects=True)
    client.post('/lists/ListB/tasks', data={'task_description': 'TaskB1'}, follow_redirects=True)

    response = client.get('/')
    assert response.status_code == 200
    assert b'ListA' in response.data
    assert b'TaskA1' in response.data
    assert b'ListB' in response.data
    assert b'TaskB1' in response.data
