"""Search Strategy Implementation i.e keyword, tag and user search"""

from abc import ABC, abstractmethod
from low_level_design.practice_problems.design_stack_overflow.src.entities.question import Question
from typing import List
class SearchStrategy(ABC):
    @abstractmethod
    def search(self, questions: List[Question]) -> List[Question]:
        pass