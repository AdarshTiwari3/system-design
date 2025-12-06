"""Answer is also Post Type"""
from low_level_design.practice_problems.design_stack_overflow.src.entities.post import Post
from low_level_design.practice_problems.design_stack_overflow.src.entities.user import User
from uuid import uuid4
class Answer(Post):
    def __init__(self, body: str, author: User):
        super().__init__(str(uuid4()), body, author)
        self._is_accepted_answer : bool =False

    def set_accepted_answer(self, accepted: bool):
        self._is_accepted_answer=accepted

    @property
    def is_accepted_answer(self) -> bool:
        return self._is_accepted_answer
    