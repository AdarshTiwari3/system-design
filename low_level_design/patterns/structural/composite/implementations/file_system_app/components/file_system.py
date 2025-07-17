""" interface"""

from abc import ABC, abstractmethod

class FileSystemInterface(ABC):
    @abstractmethod
    def ls(self, indent: int = 0)-> None:
        pass
