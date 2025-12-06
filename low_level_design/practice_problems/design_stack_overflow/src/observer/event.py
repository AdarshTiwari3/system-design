"""Event Class Means publisher"""
from low_level_design.practice_problems.design_stack_overflow.src.enums.event_type import EventType
from low_level_design.practice_problems.design_stack_overflow.src.entities.user import User
from low_level_design.practice_problems.design_stack_overflow.src.entities.post import Post
class Event:
    def __init__(self, event_type: EventType, publisher: User, target_post: Post ): # can also be called subject or actor
        self.event_type=event_type
        self.publisher=publisher
        self.target_post=target_post


    def get_publisher(self) -> User:
        return self.publisher
    
    def get_event_type(self) -> EventType:
        return self.event_type
    
    def get_target_post(self) -> Post:
        return self.target_post