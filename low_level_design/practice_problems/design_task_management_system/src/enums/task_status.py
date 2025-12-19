from enum import Enum
"""
PENDING → IN_PROGRESS → COMPLETED
           ↕
        BLOCKED

"""
class TaskStatus(Enum):
    IN_PROGRESS='IN_PROGRESS'
    COMPLETED='COMPLETED'
    PENDING='PENDING'
    BLOCKED='BLOCKED'

    def is_terminal(self) -> bool:
        """Life cycle completed- means in completed status"""
        return self in {TaskStatus.COMPLETED}