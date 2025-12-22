from datetime import datetime

class ActivityLog:
    def __init__(self, description: str):
        self._description = description
        self._timestamp = datetime.now()

    def __str__(self) -> str: #prints object like print(obj) - [2025-08-20 14:35:10.123456] - Task moved to IN_PROGRESS
        return f"[{self._timestamp}] - {self._description}"

    def __repr__(self):
        return f"ActivityLog(description={self._description!r}, timestamp={self._timestamp!r})"
