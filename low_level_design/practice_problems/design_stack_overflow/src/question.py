"""Question class implementation which inherits some property of Post class as it is also a post type"""
from post import Post
from user import User
from tag import Tag
from answer import Answer
from event import Event
from event_type import EventType
from typing import List, Set, Optional
from uuid import uuid4

class Question(Post):
    def __init__(self, title: str, body: str, author: User, tags: Set[Tag]):
        super().__init__(str(uuid4()), body, author)
        self.title=title
        self.tags=tags
        self.answers: List[Answer]=[]
        self.accepted_answer: Optional[Answer] = None

    def add_answer(self, answer: Answer) -> None:
        self.answers.append(answer)

    def get_title(self) -> str:
        return self.title
    
    def get_all_tags(self) -> Set[Tag]:
        return self.tags

    def accept_answer(self, answer: Answer) -> bool:
        with self._lock:
            if self.accepted_answer:
                return False
            
            #disallowing user to accept its own answer
            if answer.get_content_author().get_user_id() == self.get_content_author().get_user_id():
                return False
            
            if answer not in self.answers:
                self.answers.append(answer)
            
            self.accepted_answer = answer

            answer.set_accepted_answer(True)

            event = Event(EventType.ACCEPT_ANSWER, self.get_content_author(), answer)

            self.notify_observer(event)
            
            return True

    def get_accepted_answer(self) -> Optional[Answer]:
        return self.accepted_answer
    
    def get_all_answers(self) -> List[Answer]:
        return self.answers