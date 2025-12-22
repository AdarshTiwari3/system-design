"""Task List Class Implementation"""
from uuid import uuid4
from typing import List
from core.task import Task
import threading

class TaskList:
    def __init__(self, name: str):
        if not name:
            raise ValueError("TaskList name cannot be empty")
        
        self._id=str(uuid4())
        self._name=name
        self._tasks: List[Task]=[]
        self._lock=threading.Lock()

    def add_task(self, task: Task):
        with self._lock:
            self._tasks.append(task)

    def remove_task(self, task) -> bool:
        with self._lock:
            if task in self._tasks:
                self._tasks.remove(task)
                return True
            return False
    def get_tasks(self) -> List[Task]:
        with self._lock:
            return self._tasks.copy() # to avoid any external modification we can also use list(self._tasks)
        
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    