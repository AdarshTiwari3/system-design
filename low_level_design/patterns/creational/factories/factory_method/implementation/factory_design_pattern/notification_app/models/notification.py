'''Product class '''

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass