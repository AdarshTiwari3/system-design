from enum import Enum

class TaskPriority(Enum):
    LOW = ("LOW", 1)
    MEDIUM = ("MEDIUM", 2)
    HIGH = ("HIGH", 3)
    CRITICAL = ("CRITICAL", 4)


    @property
    def label(self) -> str:
        return self.value[0]

    @property
    def level(self) -> int:
        return self.value[1]