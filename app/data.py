"""Data models and persistence layer for to-do lists and tasks."""
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict, field
import json


@dataclass
class Task:
    """Represents a task in a to-do list."""
    id: str
    text: str
    completed: bool = False
    list_id: Optional[str] = None
    
    def to_dict(self):
        """Convert task to dictionary."""
        return asdict(self)


@dataclass
class TodoList:
    """Represents a to-do list containing multiple tasks."""
    id: str
    name: str
    tasks: List[Task] = field(default_factory=list)
    
    def to_dict(self):
        """Convert list to dictionary with tasks included."""
        return {
            'id': self.id,
            'name': self.name,
            'tasks': [task.to_dict() for task in self.tasks]
        }


class DataStore:
    """In-memory data store for lists and tasks.
    
    Provides CRUD operations for managing to-do lists and their tasks.
    Data is session-scoped (clears on server restart).
    """
    
    def __init__(self):
        """Initialize the data store."""
        self.lists: Dict[str, TodoList] = {}
        self._next_list_id = 1
        self._next_task_id = 1
    
    # ========== List Operations ==========
    
    def create_list(self, name: str) -> TodoList:
        """Create a new to-do list.
        
        Args:
            name: The name of the list (must be non-empty, max 255 chars)
            
        Returns:
            The created TodoList object
            
        Raises:
            ValueError: If name is empty or too long
        """
        if not name or not name.strip():
            raise ValueError("List name cannot be empty")
        if len(name) > 255:
            raise ValueError("List name must be 255 characters or less")
        
        list_id = str(self._next_list_id)
        self._next_list_id += 1
        
        new_list = TodoList(id=list_id, name=name.strip())
        self.lists[list_id] = new_list
        return new_list
    
    def get_list(self, list_id: str) -> Optional[TodoList]:
        """Retrieve a list by ID.
        
        Args:
            list_id: The ID of the list
            
        Returns:
            The TodoList object if found, None otherwise
        """
        return self.lists.get(list_id)
    
    def get_all_lists(self) -> List[TodoList]:
        """Retrieve all lists.
        
        Returns:
            List of all TodoList objects
        """
        return list(self.lists.values())
    
    def delete_list(self, list_id: str) -> bool:
        """Delete a list and all its tasks (cascade delete).
        
        Args:
            list_id: The ID of the list to delete
            
        Returns:
            True if list was deleted, False if it didn't exist
        """
        if list_id in self.lists:
            del self.lists[list_id]
            return True
        return False
    
    # ========== Task Operations ==========
    
    def create_task(self, list_id: str, text: str) -> Task:
        """Create a new task in a list.
        
        Args:
            list_id: The ID of the list to add the task to
            text: The task text (must be non-empty, max 500 chars)
            
        Returns:
            The created Task object
            
        Raises:
            ValueError: If text is empty/too long or list doesn't exist
        """
        # Validate list exists
        todo_list = self.get_list(list_id)
        if not todo_list:
            raise ValueError(f"List with ID {list_id} not found")
        
        # Validate task text
        if not text or not text.strip():
            raise ValueError("Task text cannot be empty")
        if len(text) > 500:
            raise ValueError("Task text must be 500 characters or less")
        
        task_id = str(self._next_task_id)
        self._next_task_id += 1
        
        new_task = Task(
            id=task_id,
            text=text.strip(),
            completed=False,
            list_id=list_id
        )
        todo_list.tasks.append(new_task)
        return new_task
    
    def get_task(self, list_id: str, task_id: str) -> Optional[Task]:
        """Retrieve a specific task from a list.
        
        Args:
            list_id: The ID of the list
            task_id: The ID of the task
            
        Returns:
            The Task object if found, None otherwise
        """
        todo_list = self.get_list(list_id)
        if not todo_list:
            return None
        
        for task in todo_list.tasks:
            if task.id == task_id:
                return task
        return None
    
    def get_tasks_in_list(self, list_id: str) -> Optional[List[Task]]:
        """Retrieve all tasks in a list.
        
        Args:
            list_id: The ID of the list
            
        Returns:
            List of Task objects if list exists, None if list not found
        """
        todo_list = self.get_list(list_id)
        if todo_list is None:
            return None
        return todo_list.tasks
    
    def update_task(self, list_id: str, task_id: str, completed: bool) -> bool:
        """Update a task's completion status.
        
        Args:
            list_id: The ID of the list
            task_id: The ID of the task
            completed: The new completion status
            
        Returns:
            True if task was updated, False if task not found
        """
        task = self.get_task(list_id, task_id)
        if task:
            task.completed = completed
            return True
        return False
    
    def delete_task(self, list_id: str, task_id: str) -> bool:
        """Delete a task from a list.
        
        Args:
            list_id: The ID of the list
            task_id: The ID of the task
            
        Returns:
            True if task was deleted, False if task not found
        """
        todo_list = self.get_list(list_id)
        if not todo_list:
            return False
        
        for i, task in enumerate(todo_list.tasks):
            if task.id == task_id:
                todo_list.tasks.pop(i)
                return True
        return False
