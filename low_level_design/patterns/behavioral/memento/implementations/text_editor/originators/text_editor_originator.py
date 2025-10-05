"""Text Editor Originator implementation"""

from originators.originator_base import OriginatorInterface
from memento.memento_base import MementoBase
from memento.editor_memento import EditorMemento

class TextEditor(OriginatorInterface):
    def __init__(self):
        self._content: str = ""

    def write(self, text):
        self._content+=text

    def get_content(self) -> str:
        return self._content
    
    def save(self) -> MementoBase:
        return EditorMemento(self._content)
    
    def restore(self, memento: MementoBase) -> None:
        if memento is None:
            self._content = ""
            return
        self._content=memento.get_saved_content()
            
    
