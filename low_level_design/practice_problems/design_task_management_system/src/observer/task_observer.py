"""Task Observer- Interface"""

from abc import ABC, abstractmethod
from core.task import Task
from enums.task_event_type import TaskEventType
class TaskObserver(ABC):
    @abstractmethod
    def update(self, task: Task, event_type: TaskEventType):
        pass