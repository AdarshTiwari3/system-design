"""Cut command implementation
Here basically we remove the selected text and put it inside the clipboard of text editor
when we undo it then push it back and reset the clipboard

"""
from commands.command import Command
from core.text_editor import TextEditor
class CutCommand(Command):
    undoable = True #class variable which tells this command is undoable
    def __init__(self, text_editor: TextEditor, start: int, length: int) -> None:
        self._editor=text_editor
        self._start=start
        self._length=length
        self._cut_text: str= ""

    def execute(self):
        """cut the text from the correct position"""
        self._cut_text=self._editor.content[self._start:self._start+self._length]
        self._editor.clipboard=self._cut_text
        self._editor.delete(self._start, self._length)


    def undo(self):
        if self._cut_text:
            """put at the correct position for undo case"""
            self._editor.insert(self._cut_text, self._start)
            self._editor.clipboard=""