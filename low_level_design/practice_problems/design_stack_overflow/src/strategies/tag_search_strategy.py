"""Tag Search Strategy Implementation"""

from low_level_design.practice_problems.design_stack_overflow.src.strategies.search_strategy import SearchStrategy
from low_level_design.practice_problems.design_stack_overflow.src.entities.tag import Tag
from low_level_design.practice_problems.design_stack_overflow.src.entities.question import Question
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