"""Search Strategy Implementation i.e keyword, tag and user search"""

from abc import ABC, abstractmethod
from entities.question import Question
from typing import List
class SearchStrategy(ABC):
    @abstractmethod
    def search(self, questions: List[Question]) -> List[Question]:
        pass