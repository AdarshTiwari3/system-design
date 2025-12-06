"""Stackoverflow Post implementation"""
"""Why are using content here, because we features are common in comment post question and answer"""
from low_level_design.practice_problems.design_stack_overflow.src.entities.content import Content
from low_level_design.practice_problems.design_stack_overflow.src.entities.user import User
from typing import Dict, List
from low_level_design.practice_problems.design_stack_overflow.src.enums.vote_type import VoteType
from low_level_design.practice_problems.design_stack_overflow.src.entities.comments import Comment
from low_level_design.practice_problems.design_stack_overflow.src.observer.post_observer import PostObserver
import threading
from low_level_design.practice_problems.design_stack_overflow.src.entities.question import Question
from low_level_design.practice_problems.design_stack_overflow.src.enums.event_type import EventType
from low_level_design.practice_problems.design_stack_overflow.src.observer.event import Event

class Post(Content):
    def __init__(self, content_id: str, body: str, author: User): #we have not used post id because post id is content id so why to keep two names 
        super().__init__(content_id, body, author)
        self.count_vote: int=0
        self.voters: Dict[str, VoteType]={}
        self.comments: List[Comment]=[]
        self.observers: List[PostObserver]=[]
        self._lock=threading.Lock()


    def add_observer(self, observer: PostObserver):
        self.observers.append(observer)

    def notify_observer(self, event: Event):
        # notify all the observer or subscriber
        for observer in self.observers:
            observer.update_on_post(event)

    def get_vote_count(self) -> int:
        return self.count_vote
    
    def get_comment(self) -> List[Comment]:
        return self.comments
    
    def add_comment(self, new_comment: Comment):
        self.comments.append(new_comment)

    def vote(self, user: User, vote_type: VoteType):
        #perform voting on a post
        with self._lock:
            userid=user.get_user_id()

            if self.voters.get(userid) == vote_type:
                #already vote is casted
                return 
            new_score=0

            if userid in self.voters:
                if vote_type == VoteType.UPVOTE:
                    #means it was already downvoted so new change will be +2 
                    new_score=2
                else: 
                    #means already upvoted so new change will be -2 because -1 will be real and new -1 so total -2
                
                    new_score=-2

            else:
                new_score= 1 if vote_type == VoteType.UPVOTE else -1

            """Update the vote count and voters dictionary"""
            self.count_vote+=new_score
            self.voters[userid]=vote_type

            if isinstance(self, Question):
                event_type=EventType.UPVOTE_QUESTION if vote_type == VoteType.UPVOTE else EventType.DOWNVOTE_QUESTION

            else:
                #answer object type
                event_type=EventType.UPVOTE_ANSWER if vote_type == VoteType.UPVOTE else EventType.DOWNVOTE_ANSWER

            """Notify the observer"""
            new_event=Event(event_type,user,self) #here self represents Post
            self.notify_observer(new_event)