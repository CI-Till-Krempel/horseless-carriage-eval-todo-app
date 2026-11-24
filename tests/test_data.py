"""Unit tests for the data model (US-0002)."""
import pytest
from app.data import Task, TodoList, DataStore


class TestDataStore:
    """Test suite for DataStore CRUD operations."""
    
    @pytest.fixture
    def store(self):
        """Create a fresh DataStore instance for each test."""
        return DataStore()
    
    # ========== List Tests ==========
    
    def test_create_list_success(self, store):
        """Test creating a list with valid name."""
        list_obj = store.create_list("Shopping")
        assert list_obj.id == "1"
        assert list_obj.name == "Shopping"
        assert list_obj.tasks == []
    
    def test_create_multiple_lists_increments_ids(self, store):
        """Test that list IDs increment correctly."""
        list1 = store.create_list("Shopping")
        list2 = store.create_list("Work")
        list3 = store.create_list("Home")
        
        assert list1.id == "1"
        assert list2.id == "2"
        assert list3.id == "3"
    
    def test_create_list_empty_name_raises_error(self, store):
        """Test that empty list name raises ValueError."""
        with pytest.raises(ValueError, match="List name cannot be empty"):
            store.create_list("")
        
        with pytest.raises(ValueError, match="List name cannot be empty"):
            store.create_list("   ")  # Whitespace only
    
    def test_create_list_name_too_long_raises_error(self, store):
        """Test that name exceeding 255 chars raises ValueError."""
        long_name = "a" * 256
        with pytest.raises(ValueError, match="List name must be 255 characters or less"):
            store.create_list(long_name)
    
    def test_create_list_name_trimmed(self, store):
        """Test that list names are trimmed of leading/trailing whitespace."""
        list_obj = store.create_list("  Shopping  ")
        assert list_obj.name == "Shopping"
    
    def test_get_list_found(self, store):
        """Test retrieving an existing list."""
        created = store.create_list("Shopping")
        retrieved = store.get_list("1")
        
        assert retrieved is not None
        assert retrieved.id == created.id
        assert retrieved.name == created.name
    
    def test_get_list_not_found(self, store):
        """Test retrieving a non-existent list."""
        result = store.get_list("999")
        assert result is None
    
    def test_get_all_lists_empty(self, store):
        """Test retrieving all lists when store is empty."""
        lists = store.get_all_lists()
        assert lists == []
    
    def test_get_all_lists_multiple(self, store):
        """Test retrieving all lists."""
        list1 = store.create_list("Shopping")
        list2 = store.create_list("Work")
        list3 = store.create_list("Home")
        
        all_lists = store.get_all_lists()
        assert len(all_lists) == 3
        assert list1 in all_lists
        assert list2 in all_lists
        assert list3 in all_lists
    
    def test_delete_list_success(self, store):
        """Test deleting an existing list."""
        store.create_list("Shopping")
        result = store.delete_list("1")
        
        assert result is True
        assert store.get_list("1") is None
    
    def test_delete_list_not_found(self, store):
        """Test deleting a non-existent list."""
        result = store.delete_list("999")
        assert result is False
    
    def test_delete_list_cascade_deletes_tasks(self, store):
        """Test that deleting a list also deletes all its tasks."""
        list_obj = store.create_list("Shopping")
        store.create_task("1", "Milk")
        store.create_task("1", "Bread")
        
        assert len(list_obj.tasks) == 2
        
        store.delete_list("1")
        retrieved = store.get_list("1")
        assert retrieved is None
    
    # ========== Task Tests ==========
    
    def test_create_task_success(self, store):
        """Test creating a task in a list."""
        store.create_list("Shopping")
        task = store.create_task("1", "Buy milk")
        
        assert task.id == "1"
        assert task.text == "Buy milk"
        assert task.completed is False
        assert task.list_id == "1"
    
    def test_create_task_multiple_increments_ids(self, store):
        """Test that task IDs increment correctly."""
        store.create_list("Shopping")
        task1 = store.create_task("1", "Milk")
        task2 = store.create_task("1", "Bread")
        task3 = store.create_task("1", "Eggs")
        
        assert task1.id == "1"
        assert task2.id == "2"
        assert task3.id == "3"
    
    def test_create_task_in_nonexistent_list_raises_error(self, store):
        """Test that creating a task in non-existent list raises error."""
        with pytest.raises(ValueError, match="List with ID 999 not found"):
            store.create_task("999", "Task")
    
    def test_create_task_empty_text_raises_error(self, store):
        """Test that empty task text raises ValueError."""
        store.create_list("Shopping")
        
        with pytest.raises(ValueError, match="Task text cannot be empty"):
            store.create_task("1", "")
        
        with pytest.raises(ValueError, match="Task text cannot be empty"):
            store.create_task("1", "   ")  # Whitespace only
    
    def test_create_task_text_too_long_raises_error(self, store):
        """Test that task text exceeding 500 chars raises ValueError."""
        store.create_list("Shopping")
        long_text = "a" * 501
        
        with pytest.raises(ValueError, match="Task text must be 500 characters or less"):
            store.create_task("1", long_text)
    
    def test_create_task_text_trimmed(self, store):
        """Test that task text is trimmed of leading/trailing whitespace."""
        store.create_list("Shopping")
        task = store.create_task("1", "  Buy milk  ")
        assert task.text == "Buy milk"
    
    def test_get_task_found(self, store):
        """Test retrieving an existing task."""
        store.create_list("Shopping")
        created = store.create_task("1", "Buy milk")
        retrieved = store.get_task("1", "1")
        
        assert retrieved is not None
        assert retrieved.id == created.id
        assert retrieved.text == created.text
    
    def test_get_task_not_found_wrong_task_id(self, store):
        """Test retrieving a non-existent task."""
        store.create_list("Shopping")
        store.create_task("1", "Buy milk")
        
        result = store.get_task("1", "999")
        assert result is None
    
    def test_get_task_list_not_found(self, store):
        """Test retrieving a task from non-existent list."""
        result = store.get_task("999", "1")
        assert result is None
    
    def test_get_tasks_in_list_empty(self, store):
        """Test retrieving tasks from empty list."""
        store.create_list("Shopping")
        tasks = store.get_tasks_in_list("1")
        
        assert tasks is not None
        assert tasks == []
    
    def test_get_tasks_in_list_multiple(self, store):
        """Test retrieving all tasks in a list."""
        store.create_list("Shopping")
        task1 = store.create_task("1", "Milk")
        task2 = store.create_task("1", "Bread")
        
        tasks = store.get_tasks_in_list("1")
        assert len(tasks) == 2
        assert task1 in tasks
        assert task2 in tasks
    
    def test_get_tasks_in_list_not_found(self, store):
        """Test retrieving tasks from non-existent list."""
        result = store.get_tasks_in_list("999")
        assert result is None
    
    def test_update_task_completion_status(self, store):
        """Test updating a task's completion status."""
        store.create_list("Shopping")
        task = store.create_task("1", "Buy milk")
        assert task.completed is False
        
        # Mark as completed
        result = store.update_task("1", "1", True)
        assert result is True
        
        retrieved = store.get_task("1", "1")
        assert retrieved.completed is True
        
        # Mark as incomplete
        result = store.update_task("1", "1", False)
        assert result is True
        
        retrieved = store.get_task("1", "1")
        assert retrieved.completed is False
    
    def test_update_task_not_found(self, store):
        """Test updating a non-existent task."""
        store.create_list("Shopping")
        result = store.update_task("1", "999", True)
        assert result is False
    
    def test_delete_task_success(self, store):
        """Test deleting a task."""
        store.create_list("Shopping")
        store.create_task("1", "Milk")
        store.create_task("1", "Bread")
        
        list_obj = store.get_list("1")
        assert len(list_obj.tasks) == 2
        
        result = store.delete_task("1", "1")
        assert result is True
        assert len(list_obj.tasks) == 1
        assert store.get_task("1", "1") is None
    
    def test_delete_task_not_found(self, store):
        """Test deleting a non-existent task."""
        store.create_list("Shopping")
        result = store.delete_task("1", "999")
        assert result is False
    
    def test_delete_task_from_nonexistent_list(self, store):
        """Test deleting a task from non-existent list."""
        result = store.delete_task("999", "1")
        assert result is False
    
    # ========== Integration Tests ==========
    
    def test_full_workflow(self, store):
        """Test a complete workflow: create lists, add tasks, toggle, delete."""
        # Create lists
        shopping = store.create_list("Shopping")
        work = store.create_list("Work")
        
        # Add tasks to shopping list
        milk = store.create_task(shopping.id, "Buy milk")
        bread = store.create_task(shopping.id, "Buy bread")
        
        # Add task to work list
        report = store.create_task(work.id, "Write report")
        
        # Verify counts
        assert len(store.get_all_lists()) == 2
        assert len(store.get_tasks_in_list(shopping.id)) == 2
        assert len(store.get_tasks_in_list(work.id)) == 1
        
        # Mark milk as complete
        store.update_task(shopping.id, milk.id, True)
        assert store.get_task(shopping.id, milk.id).completed is True
        
        # Delete bread task
        store.delete_task(shopping.id, bread.id)
        assert len(store.get_tasks_in_list(shopping.id)) == 1
        
        # Delete work list (cascade)
        store.delete_list(work.id)
        assert store.get_list(work.id) is None
        assert len(store.get_all_lists()) == 1
    
    def test_data_persistence_in_memory(self, store):
        """Test that data persists in memory across operations."""
        # Create data
        shopping = store.create_list("Shopping")
        milk = store.create_task(shopping.id, "Buy milk")
        
        # Retrieve and verify persistence
        retrieved_list = store.get_list(shopping.id)
        assert retrieved_list.name == "Shopping"
        
        retrieved_task = store.get_task(shopping.id, milk.id)
        assert retrieved_task.text == "Buy milk"
        
        # Modify and verify
        store.update_task(shopping.id, milk.id, True)
        modified_task = store.get_task(shopping.id, milk.id)
        assert modified_task.completed is True
    
    def test_to_dict_conversions(self, store):
        """Test that objects convert to dictionaries correctly."""
        list_obj = store.create_list("Shopping")
        task1 = store.create_task(list_obj.id, "Milk")
        task2 = store.create_task(list_obj.id, "Bread")
        
        list_dict = list_obj.to_dict()
        assert list_dict['id'] == list_obj.id
        assert list_dict['name'] == "Shopping"
        assert len(list_dict['tasks']) == 2
        
        task_dict = task1.to_dict()
        assert task_dict['id'] == task1.id
        assert task_dict['text'] == "Milk"
        assert task_dict['completed'] is False
