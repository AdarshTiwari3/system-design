from enums.task_status import TaskStatus
from typing import Optional, List
from datetime import date
from entities.user import User
from enums.task_priority import TaskPriority
from uuid import uuid4
from entities.comment import Comment
from entities.tag import Tag

class Task:
    def __init__(self, title: str, description: str = "", due_date: Optional[date]=None, priority: TaskPriority=TaskPriority.MEDIUM, assignee: Optional[User] =None):
        if not title:
            raise ValueError("Task title cannot be empty")

        self._id=str(uuid4())
        self._title=title
        self._description=description
        self._due_date=due_date
        self._priority=priority
        self._status=TaskStatus.PENDING
        self._assignee=assignee
        self._version=0 # to cound how many times it has been modified( optimistic locking)
        self._comments: List[Comment] = []
        self._tags: set[Tag] = set()

    
    #getters
    @property
    def status(self) -> TaskStatus:
        return self._status
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def title(self) -> str:
        return self._title
    
    @property
    def description(self):
        return self._description
    
    @property
    def due_date(self) -> Optional[date]:
        return self._due_date
    
    @property
    def priority(self) -> TaskPriority:
        return self._priority

    @property
    def assignee(self) -> Optional[User]:
        return self._assignee
    
    @property
    def version(self) -> int:
        return self._version
    
    @property
    def comments(self):
        return self._comments.copy()

    @property
    def tags(self):
        return self._tags.copy()
    
    #controlled mutation / setter
    """version is incremented on every state-changing operation because it represents the version of the Task as a whole"""
    
    def _set_status(self, status: TaskStatus):
        self._status=status
        self._version += 1 #version changed

    def _set_priority(self, priority: TaskPriority):
        self._priority=priority
        self._version += 1 # again version changed

    def _assign(self, user: User):
        self._assignee = user
        self._version += 1 # version changed

    def add_comment(self, comment: Comment):
        self._comments.append(comment)

    def add_tag(self, tag: Tag):
        self._tags.add(tag)
