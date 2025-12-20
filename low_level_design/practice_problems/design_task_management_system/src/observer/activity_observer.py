"""Activity Observer- concrete class"""

from observer.task_observer import TaskObserver

class ActivityObserver(TaskObserver):
    def update(self, task, event_type):
        event = event_type.value if hasattr(event_type, "value") else event_type #checks if event type has enum values or not
        print(f"Logger - Task '{task.get_title()}' was changed, change={event}")
