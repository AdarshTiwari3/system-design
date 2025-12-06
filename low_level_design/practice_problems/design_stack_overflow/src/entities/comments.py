"""Comment class implementation which is a Content type class"""

from low_level_design.practice_problems.design_stack_overflow.src.entities.content import Content
from uuid import uuid4 
class Comment(Content):
    def __init__(self, body, author):
        super().__init__(str(uuid4()), body, author)