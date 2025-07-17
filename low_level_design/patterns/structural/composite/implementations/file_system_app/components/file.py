"""Leaf Node"""

from components.file_system import FileSystemInterface

class File(FileSystemInterface):
    def __init__(self, file_name: str):
        # get the file name
        self._file_name= file_name
    def ls(self, indent: int = 0) -> None:
        print(" "*indent + f"📄 {self._file_name}")
