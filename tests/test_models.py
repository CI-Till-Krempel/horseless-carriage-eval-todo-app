"""
Unit tests for data models (List, Task, DataStore).
Tests all CRUD operations and validation.
"""

import pytest
from app.models import Task, List, DataStore


class TestTask:
    """Test the Task model."""
    
    def test_task_creation(self):
        """Test creating a task."""
        task = Task(text="Buy milk", list_id="list-1")
        assert task.text == "Buy milk"
        assert task.list_id == "list-1"
        assert task.completed is False
        assert task.id is not None
        assert task.created_at is not None
    
    def test_task_with_explicit_id(self):
        """Test creating a task with an explicit ID."""
        task = Task(text="Buy milk", list_id="list-1", task_id="task-123")
        assert task.id == "task-123"
    
    def test_task_completion_toggle(self):
        """Test toggling task completion status."""
        task = Task(text="Buy milk", list_id="list-1")
        assert task.completed is False
        task.completed = True
        assert task.completed is True
    
    def test_task_to_dict(self):
        """Test converting task to dictionary."""
        task = Task(text="Buy milk", list_id="list-1", task_id="task-123")
        task_dict = task.to_dict()
        assert task_dict['id'] == "task-123"
        assert task_dict['text'] == "Buy milk"
        assert task_dict['list_id'] == "list-1"
        assert task_dict['completed'] is False
        assert 'created_at' in task_dict
    
    def test_task_from_dict(self):
        """Test creating a task from dictionary."""
        data = {
            'id': 'task-123',
            'text': 'Buy milk',
            'list_id': 'list-1',
            'completed': True
        }
        task = Task.from_dict(data)
        assert task.id == 'task-123'
        assert task.text == 'Buy milk'
        assert task.list_id == 'list-1'
        assert task.completed is True


class TestList:
    """Test the List model."""
    
    def test_list_creation(self):
        """Test creating a list."""
        lst = List(name="Groceries")
        assert lst.name == "Groceries"
        assert lst.id is not None
        assert lst.tasks == []
        assert lst.created_at is not None
    
    def test_list_with_explicit_id(self):
        """Test creating a list with an explicit ID."""
        lst = List(name="Groceries", list_id="list-123")
        assert lst.id == "list-123"
    
    def test_add_task_to_list(self):
        """Test adding a task to a list."""
        lst = List(name="Groceries", list_id="list-1")
        task = Task(text="Buy milk", list_id="list-1")
        lst.add_task(task)
        assert len(lst.tasks) == 1
        assert lst.tasks[0].id == task.id
    
    def test_add_task_with_mismatched_list_id_raises_error(self):
        """Test that adding a task with mismatched list_id raises an error."""
        lst = List(name="Groceries", list_id="list-1")
        task = Task(text="Buy milk", list_id="list-2")  # Different list ID
        with pytest.raises(ValueError, match="list_id"):
            lst.add_task(task)
    
    def test_get_task_from_list(self):
        """Test retrieving a task from a list."""
        lst = List(name="Groceries", list_id="list-1")
        task = Task(text="Buy milk", list_id="list-1", task_id="task-1")
        lst.add_task(task)
        
        retrieved = lst.get_task("task-1")
        assert retrieved is not None
        assert retrieved.id == "task-1"
        assert retrieved.text == "Buy milk"
    
    def test_get_nonexistent_task_returns_none(self):
        """Test that getting a nonexistent task returns None."""
        lst = List(name="Groceries", list_id="list-1")
        assert lst.get_task("nonexistent") is None
    
    def test_remove_task_from_list(self):
        """Test removing a task from a list."""
        lst = List(name="Groceries", list_id="list-1")
        task = Task(text="Buy milk", list_id="list-1", task_id="task-1")
        lst.add_task(task)
        assert len(lst.tasks) == 1
        
        removed = lst.remove_task("task-1")
        assert removed is True
        assert len(lst.tasks) == 0
    
    def test_remove_nonexistent_task_returns_false(self):
        """Test that removing a nonexistent task returns False."""
        lst = List(name="Groceries", list_id="list-1")
        removed = lst.remove_task("nonexistent")
        assert removed is False
    
    def test_list_to_dict(self):
        """Test converting list to dictionary."""
        lst = List(name="Groceries", list_id="list-1")
        task = Task(text="Buy milk", list_id="list-1", task_id="task-1")
        lst.add_task(task)
        
        lst_dict = lst.to_dict()
        assert lst_dict['id'] == "list-1"
        assert lst_dict['name'] == "Groceries"
        assert len(lst_dict['tasks']) == 1
        assert lst_dict['tasks'][0]['text'] == "Buy milk"
    
    def test_list_to_dict_without_tasks(self):
        """Test converting list to dictionary without including tasks."""
        lst = List(name="Groceries", list_id="list-1")
        task = Task(text="Buy milk", list_id="list-1", task_id="task-1")
        lst.add_task(task)
        
        lst_dict = lst.to_dict(include_tasks=False)
        assert lst_dict['tasks'] == []
    
    def test_list_from_dict(self):
        """Test creating a list from dictionary."""
        data = {
            'id': 'list-1',
            'name': 'Groceries',
            'tasks': [
                {'id': 'task-1', 'text': 'Buy milk', 'list_id': 'list-1', 'completed': False}
            ]
        }
        lst = List.from_dict(data)
        assert lst.id == 'list-1'
        assert lst.name == 'Groceries'
        assert len(lst.tasks) == 1
        assert lst.tasks[0].text == 'Buy milk'


class TestDataStore:
    """Test the DataStore class."""
    
    @pytest.fixture
    def store(self):
        """Create a fresh DataStore for each test."""
        return DataStore()
    
    def test_create_list(self, store):
        """Test creating a list in the data store."""
        lst = store.create_list("Groceries")
        assert lst.name == "Groceries"
        assert lst.id is not None
    
    def test_create_list_with_empty_name_raises_error(self, store):
        """Test that creating a list with empty name raises an error."""
        with pytest.raises(ValueError, match="cannot be empty"):
            store.create_list("")
    
    def test_create_list_with_whitespace_only_raises_error(self, store):
        """Test that creating a list with whitespace-only name raises an error."""
        with pytest.raises(ValueError, match="cannot be empty"):
            store.create_list("   ")
    
    def test_create_list_with_long_name_raises_error(self, store):
        """Test that creating a list with name > 255 chars raises an error."""
        long_name = "a" * 256
        with pytest.raises(ValueError, match="255 characters"):
            store.create_list(long_name)
    
    def test_get_list(self, store):
        """Test retrieving a list from the data store."""
        created = store.create_list("Groceries")
        retrieved = store.get_list(created.id)
        assert retrieved is not None
        assert retrieved.id == created.id
        assert retrieved.name == "Groceries"
    
    def test_get_nonexistent_list_returns_none(self, store):
        """Test that getting a nonexistent list returns None."""
        result = store.get_list("nonexistent")
        assert result is None
    
    def test_get_all_lists(self, store):
        """Test retrieving all lists."""
        list1 = store.create_list("Groceries")
        list2 = store.create_list("Chores")
        
        all_lists = store.get_all_lists()
        assert len(all_lists) == 2
        list_ids = {lst.id for lst in all_lists}
        assert list1.id in list_ids
        assert list2.id in list_ids
    
    def test_get_all_lists_empty(self, store):
        """Test getting all lists when store is empty."""
        all_lists = store.get_all_lists()
        assert all_lists == []
    
    def test_delete_list(self, store):
        """Test deleting a list."""
        lst = store.create_list("Groceries")
        list_id = lst.id
        
        deleted = store.delete_list(list_id)
        assert deleted is True
        
        retrieved = store.get_list(list_id)
        assert retrieved is None
    
    def test_delete_nonexistent_list_returns_false(self, store):
        """Test that deleting a nonexistent list returns False."""
        deleted = store.delete_list("nonexistent")
        assert deleted is False
    
    def test_create_task(self, store):
        """Test creating a task in a list."""
        lst = store.create_list("Groceries")
        task = store.create_task(lst.id, "Buy milk")
        
        assert task is not None
        assert task.text == "Buy milk"
        assert task.list_id == lst.id
    
    def test_create_task_in_nonexistent_list_returns_none(self, store):
        """Test that creating a task in nonexistent list returns None."""
        task = store.create_task("nonexistent", "Buy milk")
        assert task is None
    
    def test_create_task_with_empty_text_raises_error(self, store):
        """Test that creating a task with empty text raises an error."""
        lst = store.create_list("Groceries")
        with pytest.raises(ValueError, match="cannot be empty"):
            store.create_task(lst.id, "")
    
    def test_create_task_with_long_text_raises_error(self, store):
        """Test that creating a task with text > 500 chars raises an error."""
        lst = store.create_list("Groceries")
        long_text = "a" * 501
        with pytest.raises(ValueError, match="500 characters"):
            store.create_task(lst.id, long_text)
    
    def test_get_task(self, store):
        """Test retrieving a task from a list."""
        lst = store.create_list("Groceries")
        created_task = store.create_task(lst.id, "Buy milk")
        
        retrieved = store.get_task(lst.id, created_task.id)
        assert retrieved is not None
        assert retrieved.text == "Buy milk"
    
    def test_get_task_in_nonexistent_list_returns_none(self, store):
        """Test that getting a task in nonexistent list returns None."""
        task = store.get_task("nonexistent", "task-id")
        assert task is None
    
    def test_get_nonexistent_task_returns_none(self, store):
        """Test that getting a nonexistent task returns None."""
        lst = store.create_list("Groceries")
        task = store.get_task(lst.id, "nonexistent")
        assert task is None
    
    def test_get_all_tasks(self, store):
        """Test retrieving all tasks in a list."""
        lst = store.create_list("Groceries")
        task1 = store.create_task(lst.id, "Buy milk")
        task2 = store.create_task(lst.id, "Buy bread")
        
        all_tasks = store.get_all_tasks(lst.id)
        assert len(all_tasks) == 2
        task_ids = {t.id for t in all_tasks}
        assert task1.id in task_ids
        assert task2.id in task_ids
    
    def test_get_all_tasks_in_nonexistent_list_returns_empty(self, store):
        """Test that getting all tasks in nonexistent list returns empty list."""
        all_tasks = store.get_all_tasks("nonexistent")
        assert all_tasks == []
    
    def test_update_task_completion(self, store):
        """Test updating task completion status."""
        lst = store.create_list("Groceries")
        task = store.create_task(lst.id, "Buy milk")
        assert task.completed is False
        
        updated = store.update_task_completion(lst.id, task.id, True)
        assert updated is not None
        assert updated.completed is True
        
        # Verify the change persisted
        retrieved = store.get_task(lst.id, task.id)
        assert retrieved.completed is True
    
    def test_update_task_completion_nonexistent_returns_none(self, store):
        """Test that updating nonexistent task returns None."""
        lst = store.create_list("Groceries")
        result = store.update_task_completion(lst.id, "nonexistent", True)
        assert result is None
    
    def test_delete_task(self, store):
        """Test deleting a task from a list."""
        lst = store.create_list("Groceries")
        task = store.create_task(lst.id, "Buy milk")
        
        deleted = store.delete_task(lst.id, task.id)
        assert deleted is True
        
        retrieved = store.get_task(lst.id, task.id)
        assert retrieved is None
    
    def test_delete_task_in_nonexistent_list_returns_false(self, store):
        """Test that deleting a task in nonexistent list returns False."""
        deleted = store.delete_task("nonexistent", "task-id")
        assert deleted is False
    
    def test_delete_nonexistent_task_returns_false(self, store):
        """Test that deleting a nonexistent task returns False."""
        lst = store.create_list("Groceries")
        deleted = store.delete_task(lst.id, "nonexistent")
        assert deleted is False
    
    def test_cascade_delete_list_with_tasks(self, store):
        """Test that deleting a list also removes its tasks."""
        lst = store.create_list("Groceries")
        task1 = store.create_task(lst.id, "Buy milk")
        task2 = store.create_task(lst.id, "Buy bread")
        
        # Verify tasks exist
        all_tasks = store.get_all_tasks(lst.id)
        assert len(all_tasks) == 2
        
        # Delete the list
        store.delete_list(lst.id)
        
        # Verify list and tasks are gone
        retrieved_list = store.get_list(lst.id)
        assert retrieved_list is None
        
        all_tasks = store.get_all_tasks(lst.id)
        assert all_tasks == []
    
    def test_multiple_lists_with_tasks(self, store):
        """Test managing multiple lists with their own tasks."""
        list1 = store.create_list("Groceries")
        list2 = store.create_list("Chores")
        
        task1 = store.create_task(list1.id, "Buy milk")
        task2 = store.create_task(list1.id, "Buy bread")
        task3 = store.create_task(list2.id, "Wash dishes")
        task4 = store.create_task(list2.id, "Vacuum")
        
        # Verify correct tasks in each list
        list1_tasks = store.get_all_tasks(list1.id)
        list2_tasks = store.get_all_tasks(list2.id)
        
        assert len(list1_tasks) == 2
        assert len(list2_tasks) == 2
        
        list1_task_ids = {t.id for t in list1_tasks}
        list2_task_ids = {t.id for t in list2_tasks}
        
        assert task1.id in list1_task_ids
        assert task2.id in list1_task_ids
        assert task3.id in list2_task_ids
        assert task4.id in list2_task_ids
