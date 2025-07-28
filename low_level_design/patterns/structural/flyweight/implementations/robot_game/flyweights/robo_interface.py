"""Robot Interface for implmentation"""

from abc import ABC, abstractmethod

class RobotInterface(ABC):

    @abstractmethod
    def display(self, context: dict) -> None:
        pass