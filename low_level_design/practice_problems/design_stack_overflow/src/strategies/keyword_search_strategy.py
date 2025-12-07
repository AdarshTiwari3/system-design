"""Keyword Search"""

from strategies.search_strategy import SearchStrategy
from entities.question import Question
from typing import List

class KeywordSearchStrategy(SearchStrategy):
    def __init__(self, keyword: str):
        self.keyword=keyword.lower()

    def search(self, questions: List[Question]) -> List[Question]:
        result=[]
        if not self.keyword:
            return result
        
        for question in questions:
            if self.keyword in question.get_title().lower() or self.keyword in question.get_content_body().lower():
                result.append(question)

        return result