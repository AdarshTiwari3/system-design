"""TaskSortStrategy- Interface"""

from abc import ABC, abstractmethod
from core.task import Task
from typing import List

class TaskSortStrategy(ABC):
    @abstractmethod
    def sort(self, tasks: List[Task]) -> List[Task]:
        pass