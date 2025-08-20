"""Paste Command Implementation- it will be a kind of insert method for content and undo will be delete method
"""
from commands.command import Command
from core.text_editor import TextEditor

class PasteCommand(Command):
    undoable = True #class variable which tells this command is undoable

    def __init__(self, text_editor:TextEditor, position: int) -> None:
        self._editor=text_editor
        self._position=position
        self._pasted_text: str=""

    def execute(self):
        """It will be an insert method, get the text from clipboard"""
        if not self._editor.clipboard:
            """nothing to paste"""
            return
        self._pasted_text=self._editor.clipboard
        self._editor.insert(self._pasted_text,self._position)

    def undo(self):
        """here undo will be a delete method of editor which will remove the pasted text"""
        if self._pasted_text:
            self._editor.delete(self._position,len(self._pasted_text))
