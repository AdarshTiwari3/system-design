"""Tag Search Strategy Implementation"""

from search_strategy import SearchStrategy
from tag import Tag
from question import Question
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