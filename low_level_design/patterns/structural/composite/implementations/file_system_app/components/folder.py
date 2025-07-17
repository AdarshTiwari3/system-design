"""Composite Node which again can have leaf and composite means file and folder and it should be type of FileSystem"""

from components.file_system import FileSystemInterface
from typing import List
class Folder(FileSystemInterface):
    def __init__(self, folder_name: str)-> None:
        # this holds again array of file system objects
        self._folder_name=folder_name
        self._children: List[FileSystemInterface] = []

    def add(self, component: FileSystemInterface)->None:
        self._children.append(component)

    def remove(self, component: FileSystemInterface) -> None:
        self._children.remove(component)

    def ls(self, indent: int = 0):
        print(" "*indent + f"📁 {self._folder_name}")
        for child in self._children:
            child.ls(indent+1) #Recursive call