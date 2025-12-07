"""User Search Strategy Implementation"""

from strategies.search_strategy import SearchStrategy
from entities.user import User
from entities.question import Question
from typing import List

class UserSearchStrategy(SearchStrategy):
    def __init__(self, user: User):
        self.user=user

    def search(self, questions: List[Question]) -> List[Question]:
        result=[]

        if not self.user:
            return result
        user_=self.user
        for question in questions:
            if question.get_content_author().get_user_id() == user_.get_user_id():
                result.append(question)

        return result