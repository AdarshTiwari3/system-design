"""Command Manager (Invoker of Command Design Pattern).
Maintains command history for undo/redo operations.
"""
from commands.command import Command
from typing import Optional

class CommandManager:
    def __init__(self) -> None:
        """Invoker: Executes commands and manages undo/redo history."""
        self.history: list[Command] = []
        self.redo_stack: list[Command] = []
        self.current_command: Optional[Command] = None

    def set_command(self, command: Command) -> None:
        """Set the current command to execute."""
        self.current_command = command

    def run_command(self) -> None:
        """Execute the current command and store it if undoable."""
        if self.current_command:
            self.current_command.execute()
            
            # Only store if undoable
            if getattr(self.current_command, "undoable", True):
                self.history.append(self.current_command)
                
        else:
            print("No command found")

    def undo(self) -> None:
        """Undo the last command if available."""
        if self.history:
            latest_command = self.history.pop()
            latest_command.undo()
            self.redo_stack.append(latest_command)

    def redo(self) -> None:
        """Redo the last undone command if available."""
        if self.redo_stack:
            latest_command = self.redo_stack.pop()
            latest_command.execute()
            self.history.append(latest_command)
