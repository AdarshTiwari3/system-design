"""Editor Momento concrete class implementation"""
from momento.momento_base import MomentoBase

class EditorMomento(MomentoBase):
    def __init__(self, content: str):
        self._content=content #must be private to achieve encapsulation with exposing internal details

    def get_saved_content(self):
        return self._content
        