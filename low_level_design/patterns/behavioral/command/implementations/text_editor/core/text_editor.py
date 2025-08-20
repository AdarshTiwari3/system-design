"""
Receiver of command design pattern
TextEditor class Implementation
"""

class TextEditor:
    """Receiver: Performs text operations like insert, delete, cut, and paste."""

    def __init__(self) -> None:
        self.content: str = ""
        self.clipboard: str = ""  # For cut/copy/paste

    def insert(self, text: str) -> None:
        """Insert text at the end of content."""
        self.content += text

    def delete(self, start: int, length: int) -> None:
        """Delete characters from content starting at `start` of given `length`."""
        self.content = self.content[:start] + self.content[start+length:]

    def show_content(self) -> str:
        """Return current editor content."""
        return self.content
