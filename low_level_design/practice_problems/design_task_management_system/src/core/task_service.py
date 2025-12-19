from enums.task_status import TaskStatus
from core.task import Task
from typing import Dict, Set
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
    
    def start(self, task: Task):
        self._transition(task, TaskStatus.IN_PROGRESS)

    def complete(self, task: Task):
        self._transition(task, TaskStatus.COMPLETED)

    def reset_to_pending(self, task: Task):
        self._transition(task, TaskStatus.PENDING)


    def _transition(self, task: Task, new_status: TaskStatus):
        current_status = task.status

        if current_status.is_terminal():
            raise Exception("Completed task cannot be modified")

        allowed_next_states = self.VALID_TRANSITIONS[current_status]

        if new_status not in allowed_next_states:
            raise Exception(
                f"Invalid transition from {current_status.value} to {new_status.value}"
            )

        task.status = new_status
        task.version += 1