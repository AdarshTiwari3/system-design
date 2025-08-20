"""Command to insert text into the TextEditor."""
from commands.command import Command
from core.text_editor import TextEditor
from typing import Optional

class InsertTextCommand(Command):
    undoable = True #class variable which tells this command is undoable
    def __init__(self, text_editor: TextEditor, text: str, position: Optional[int] = None) -> None:
        self._editor = text_editor
        self._text = text
        # if no position is passed, append to end
        self._position = position if position is not None else len(self._editor.content)

    def execute(self):
        """Insert text at the given position (default: end)."""
        self._editor.insert(self._text, self._position)

    def undo(self):
        """Undo the insertion by removing the same text from position."""
        self._editor.delete(self._position, len(self._text))
