"""Delete command concrete class implementation"""
from commands.command import Command
from core.text_editor import TextEditor

class DeleteTextCommand(Command):
    undoable = True #class variable which tells this command is undoable
    def __init__(self, text_editor: TextEditor, start: int, length: int) -> None:
        self._editor = text_editor
        self._start = start
        self._length = length
        self._deleted_text: str = ""

    def execute(self):
        """Delete text and save it for undo."""
        self._deleted_text = self._editor.content[self._start:self._start + self._length]
        self._editor.delete(self._start, self._length)

    def undo(self):
        """Restore deleted text at the original position."""
        if self._deleted_text:
            self._editor.insert(self._deleted_text, self._start)
