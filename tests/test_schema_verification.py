import pytest
from app import db, TodoList, Task

def test_db_schema_verification():
    # Verify model fields exist and match expected schema attributes to prevent OperationalErrors
    assert hasattr(TodoList, 'id')
    assert hasattr(TodoList, 'title')
    assert hasattr(Task, 'id')
    assert hasattr(Task, 'title')
    assert hasattr(Task, 'done') or hasattr(Task, 'completed')
    assert hasattr(Task, 'todo_list_id') or hasattr(Task, 'list_id')
