"""Post observer implementation"""

from abc import ABC, abstractmethod
from event import Event

class PostObserver(ABC): #the subscriber
    @abstractmethod
    def update_on_post(self, event: Event):
        pass
