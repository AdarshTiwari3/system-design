"""Activity Observer- concrete class"""

from observer.task_observer import TaskObserver
from core.activity_logs import ActivityLog
from enums.task_event_type import TaskEventType
from core.task import Task

class ActivityObserver(TaskObserver):
    def __init__(self):
        self._logs: list[ActivityLog] = []

    def update(self, task: Task, event_type: TaskEventType):
        log = ActivityLog(
            description=f"{event_type.value} on task '{task.title}'"
        )
        self._logs.append(log)
        print(log)

    def get_logs(self) -> list[ActivityLog]:
        return self._logs.copy()