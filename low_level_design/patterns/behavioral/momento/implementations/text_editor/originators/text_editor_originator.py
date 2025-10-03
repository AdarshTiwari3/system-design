"""Text Editor Originator implementation"""

from originators.originator_base import OriginatorInterface
from momento.momento_base import MomentoBase
from momento.editor_momento import EditorMomento

class TextEditor(OriginatorInterface):
    def __init__(self):
        self._content: str = ""

    def write(self, text):
        self._content+=text

    def get_content(self) -> str:
        return self._content
    
    def save(self) -> MomentoBase:
        return EditorMomento(self._content)
    
    def restore(self, momento) -> None:
        self._content=momento.get_saved_content()
    
