"""
Command Interface Implementation

1. execute() - Defines the action to perform on the Receiver.
2. undo()    - Reverts the effect of a previously executed command.

"""

from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        """Execute the command on the receiver."""
        pass

    @abstractmethod
    def undo(self):
        """Undo the effects of the command."""
        pass
