"""
Receiver of command design pattern
TextEditor class Implementation
"""
from typing import Optional

class TextEditor:
    """Receiver: Performs text operations like insert, delete, cut, and paste."""

    def __init__(self) -> None:
        self.content: str = ""
        self.clipboard: str = ""  # For cut/copy/paste

    def insert(self, text: str, position: Optional[int] = None):
        if position is None:
            self.content += text
        else:
            self.content = self.content[:position] + text + self.content[position:]


    def delete(self, start: int, length: int) -> None:
        """Delete characters from content starting at `start` of given `length`."""
        self.content = self.content[:start] + self.content[start+length:]

    def show_content(self) -> str:
        """Return current editor content."""
        return self.content
    
    
