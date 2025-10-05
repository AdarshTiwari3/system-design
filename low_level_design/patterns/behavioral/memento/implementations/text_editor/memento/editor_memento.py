"""Editor Momento concrete class implementation"""
from memento.memento_base import MementoBase

class EditorMemento(MementoBase):
    def __init__(self, content: str):
        self._content=content #must be private to achieve encapsulation without exposing internal details

    def get_saved_content(self):
        return self._content
        