"""Event Class Means publisher"""
from event_type import EventType
from user import User
from post import Post
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