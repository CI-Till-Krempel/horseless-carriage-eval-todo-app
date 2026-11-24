"""
Data models for the to-do list application.
Defines List and Task entities and provides a DataStore for in-memory persistence.
"""

from datetime import datetime
from typing import List as ListType, Optional, Dict
import uuid


class Task:
    """Represents a single task within a list."""
    
    def __init__(self, text: str, list_id: str, task_id: Optional[str] = None, completed: bool = False):
        """
        Initialize a Task.
        
        Args:
            text: The task description (non-empty string, max 500 chars)
            list_id: ID of the list this task belongs to
            task_id: Unique identifier (auto-generated if not provided)
            completed: Whether the task is completed (default: False)
        """
        self.id = task_id or str(uuid.uuid4())
        self.text = text
        self.list_id = list_id
        self.completed = completed
        self.created_at = datetime.utcnow().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary representation."""
        return {
            'id': self.id,
            'text': self.text,
            'list_id': self.list_id,
            'completed': self.completed,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Create a Task from a dictionary."""
        return cls(
            text=data['text'],
            list_id=data['list_id'],
            task_id=data.get('id'),
            completed=data.get('completed', False)
        )


class List:
    """Represents a to-do list."""
    
    def __init__(self, name: str, list_id: Optional[str] = None):
        """
        Initialize a List.
        
        Args:
            name: The name of the list (non-empty string, max 255 chars)
            list_id: Unique identifier (auto-generated if not provided)
        """
        self.id = list_id or str(uuid.uuid4())
        self.name = name
        self.tasks: ListType[Task] = []
        self.created_at = datetime.utcnow().isoformat()
    
    def add_task(self, task: Task) -> None:
        """Add a task to this list."""
        if task.list_id != self.id:
            raise ValueError(f"Task list_id {task.list_id} does not match list id {self.id}")
        self.tasks.append(task)
    
    def remove_task(self, task_id: str) -> bool:
        """
        Remove a task from this list by ID.
        
        Returns:
            True if task was removed, False if not found
        """
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(i)
                return True
        return False
    
    def get_task(self, task_id: str) -> Optional[Task]:
        """Get a task by ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def to_dict(self, include_tasks: bool = True) -> Dict:
        """Convert list to dictionary representation."""
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'tasks': [task.to_dict() for task in self.tasks] if include_tasks else []
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'List':
        """Create a List from a dictionary."""
        list_obj = cls(name=data['name'], list_id=data.get('id'))
        if 'tasks' in data:
            for task_data in data['tasks']:
                task = Task.from_dict(task_data)
                list_obj.add_task(task)
        return list_obj


class DataStore:
    """In-memory data store for lists and tasks."""
    
    def __init__(self):
        """Initialize an empty data store."""
        self._lists: Dict[str, List] = {}
    
    # List operations
    def create_list(self, name: str) -> List:
        """
        Create a new list.
        
        Args:
            name: Name for the new list
            
        Returns:
            The created List object
        """
        if not name or not name.strip():
            raise ValueError("List name cannot be empty")
        if len(name) > 255:
            raise ValueError("List name must be 255 characters or less")
        
        new_list = List(name=name)
        self._lists[new_list.id] = new_list
        return new_list
    
    def get_list(self, list_id: str) -> Optional[List]:
        """Get a list by ID."""
        return self._lists.get(list_id)
    
    def get_all_lists(self) -> ListType[List]:
        """Get all lists."""
        return list(self._lists.values())
    
    def delete_list(self, list_id: str) -> bool:
        """
        Delete a list and all its tasks.
        
        Returns:
            True if list was deleted, False if not found
        """
        if list_id in self._lists:
            del self._lists[list_id]
            return True
        return False
    
    # Task operations
    def create_task(self, list_id: str, text: str) -> Optional[Task]:
        """
        Create a new task in a list.
        
        Args:
            list_id: ID of the list to add the task to
            text: Task description
            
        Returns:
            The created Task object, or None if list not found
        """
        list_obj = self.get_list(list_id)
        if not list_obj:
            return None
        
        if not text or not text.strip():
            raise ValueError("Task text cannot be empty")
        if len(text) > 500:
            raise ValueError("Task text must be 500 characters or less")
        
        task = Task(text=text, list_id=list_id)
        list_obj.add_task(task)
        return task
    
    def get_task(self, list_id: str, task_id: str) -> Optional[Task]:
        """Get a task by ID within a specific list."""
        list_obj = self.get_list(list_id)
        if not list_obj:
            return None
        return list_obj.get_task(task_id)
    
    def get_all_tasks(self, list_id: str) -> ListType[Task]:
        """Get all tasks in a list."""
        list_obj = self.get_list(list_id)
        if not list_obj:
            return []
        return list(list_obj.tasks)
    
    def update_task_completion(self, list_id: str, task_id: str, completed: bool) -> Optional[Task]:
        """
        Update the completion status of a task.
        
        Returns:
            The updated Task object, or None if not found
        """
        task = self.get_task(list_id, task_id)
        if task:
            task.completed = completed
            return task
        return None
    
    def delete_task(self, list_id: str, task_id: str) -> bool:
        """
        Delete a task from a list.
        
        Returns:
            True if task was deleted, False if not found
        """
        list_obj = self.get_list(list_id)
        if not list_obj:
            return False
        return list_obj.remove_task(task_id)


# Global data store instance
datastore = DataStore()
