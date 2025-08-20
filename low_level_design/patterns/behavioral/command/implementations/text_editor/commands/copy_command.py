"""Copy Command Concrete Implementation of Command Interface class
A copy command will set the clipboard with text and on undo operation it will remove the text from clipboard
"""

from commands.command import Command
from core.text_editor import TextEditor

class CopyCommand(Command):
    undoable = False   # explicitly mark this as not undoable
    def __init__(self, text_editor: TextEditor, start: int, end: int) -> None:
        self._editor=text_editor
        self._start=start
        self._end=end
        self._copied_text: str=""

    def execute(self):
        self._copied_text=self._editor.content[self._start:self._end]
        self._editor.clipboard=self._copied_text

    def undo(self):
         #copy shouldn't affect undo/redo
        pass
