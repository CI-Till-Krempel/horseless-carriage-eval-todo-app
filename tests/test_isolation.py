import pytest
from app import lists, tasks

def test_isolation_first(client):
    lists['list_1'] = {'id': 'list_1', 'name': 'List 1'}
    assert len(lists) == 1

def test_isolation_second(client):
    # State should be reset by autouse fixture
    assert len(lists) == 0
    assert len(tasks) == 0
