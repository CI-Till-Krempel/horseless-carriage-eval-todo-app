import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from app import app, lists

def test_app_endpoints():
    app.config['TESTING'] = True
    client = app.test_client()
    lists.clear()

    # Test index
    res = client.get('/')
    assert res.status_code == 200

    # Test create list
    res = client.post('/lists', data={'name': 'My List'}, follow_redirects=True)
    assert res.status_code == 200
    assert b'My List' in res.data

    # Test add task
    res = client.post('/lists/1/tasks', data={'text': 'Sample Task'}, follow_redirects=True)
    assert res.status_code == 200
    assert b'Sample Task' in res.data

    # Test toggle task
    res = client.post('/tasks/1/toggle', follow_redirects=True)
    assert res.status_code == 200

    # Test delete task
    res = client.post('/tasks/1/delete', follow_redirects=True)
    assert res.status_code == 200

    # Test delete list
    res = client.post('/lists/1/delete', follow_redirects=True)
    assert res.status_code == 200
