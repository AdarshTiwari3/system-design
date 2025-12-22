from enums.task_status import TaskStatus
from core.task import Task
from typing import Dict, Set, List
from observer.task_observer import TaskObserver
from enums.task_event_type import TaskEventType
from entities.user import User

class TaskService:
    """From the current task state, which states am I allowed to move to- PENDING → IN_PROGRESS
    
    PENDING      → IN_PROGRESS
    IN_PROGRESS  → COMPLETED | BLOCKED | PENDING
    BLOCKED      → IN_PROGRESS | PENDING
    COMPLETED    → NOTHING (terminal)

    """
    VALID_TRANSITIONS: Dict[TaskStatus,Set[TaskStatus]] = {
        TaskStatus.PENDING: {TaskStatus.IN_PROGRESS},
        TaskStatus.IN_PROGRESS: {TaskStatus.COMPLETED, TaskStatus.BLOCKED, TaskStatus.PENDING},
        TaskStatus.BLOCKED: {TaskStatus.IN_PROGRESS, TaskStatus.PENDING},
        TaskStatus.COMPLETED: set()
    }
    def __init__(self):
        self._observers: List[TaskObserver] = []


    def add_observer(self, observer: TaskObserver):
        self._observers.append(observer)

    def remove_observer(self, observer: TaskObserver):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def _notify(self,task: Task, event_type: TaskEventType):
        for observer in self._observers:
            observer.update(task, event_type)

    def assign(self, task: Task, user: User ,expected_version: int):
        self._check_version(task, expected_version)
        task._assign(user)
        self._notify(task, TaskEventType.ASSIGNEE_CHANGED)


    def start(self, task: Task, expected_version: int):
        self._transition(task, TaskStatus.IN_PROGRESS, expected_version)

    def complete(self, task: Task, expected_version: int):
        self._transition(task, TaskStatus.COMPLETED,expected_version)

    def reset_to_pending(self, task: Task, expected_version: int):
        self._transition(task, TaskStatus.PENDING, expected_version)


    def _transition(self, task: Task, new_status: TaskStatus, expected_version: int):
        self._check_version(task, expected_version)

        current_status = task.status

        if current_status.is_terminal():
            raise RuntimeError("Completed task cannot be modified")

        allowed_next_states = self.VALID_TRANSITIONS[current_status]

        if new_status not in allowed_next_states:
            raise RuntimeError(
                f"Invalid transition from {current_status.value} to {new_status.value}"
            )

        task._set_status(new_status)
        self._notify(task,TaskEventType.STATUS_CHANGED)
        

    def _check_version(self, task: Task, expected_version: int): 
        """It implements optimistic locking- Has someone else modified this task since I last read it?"""

        if task.version != expected_version:
            raise RuntimeError("Concurrent modification detected")
