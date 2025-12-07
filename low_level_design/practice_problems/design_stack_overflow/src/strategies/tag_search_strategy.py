"""Tag Search Strategy Implementation"""

from strategies.search_strategy import SearchStrategy
from entities.tag import Tag
from entities.question import Question
from typing import List
class TagSearchStrategy(SearchStrategy):
    def __init__(self, tag: Tag):
        self.tag=tag

    def search(self, questions: List[Question]) -> List[Question]:
        result=[]

        if not self.tag:
            return result
        
        tag_name=self.tag.get_tag_name().lower()
        for question in questions:
            for t in question.get_all_tags():
                if t.get_tag_name().lower() == tag_name:
                    result.append(question)
                    break

        return result