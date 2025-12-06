"""Post observer implementation"""

from abc import ABC, abstractmethod
from low_level_design.practice_problems.design_stack_overflow.src.observer.event import Event

class PostObserver(ABC): #the subscriber
    @abstractmethod
    def update_on_post(self, event: Event):
        pass
