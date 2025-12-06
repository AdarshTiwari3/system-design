"""Reputation Score Manager who handles the score based on activity"""
from low_level_design.practice_problems.design_stack_overflow.src.observer.post_observer import PostObserver
from low_level_design.practice_problems.design_stack_overflow.src.observer.event import Event
from low_level_design.practice_problems.design_stack_overflow.src.enums.event_type import EventType

class ReputationScoreManager(PostObserver):
    QUESTION_UPVOTED_SCORE = 10
    ANSWER_UPVOTED_SCORE = 10
    ACCEPTED_ANSWER_SCORE = 15
    
    AUTHOR_DOWNVOTE_PENALTY = -2 #post author
    VOTER_DOWNVOTE_PENALTY = -1 # When a user downvotes an answer, the voter loses −1 reputation.

    def update_on_post(self, event: Event):
        post = event.get_target_post()
        post_author = post.get_content_author()
        voter = event.get_publisher()

        if event.get_event_type() == EventType.UPVOTE_QUESTION:
            post_author.update_reputation(self.QUESTION_UPVOTED_SCORE)

        elif event.get_event_type() == EventType.UPVOTE_ANSWER:
            post_author.update_reputation(self.ANSWER_UPVOTED_SCORE)

        elif event.get_event_type() == EventType.DOWNVOTE_QUESTION:
            post_author.update_reputation(self.AUTHOR_DOWNVOTE_PENALTY)

        elif event.get_event_type() == EventType.DOWNVOTE_ANSWER:
            post_author.update_reputation(self.AUTHOR_DOWNVOTE_PENALTY)
            voter.update_reputation(self.VOTER_DOWNVOTE_PENALTY)

        elif event.get_event_type() == EventType.ACCEPT_ANSWER:
            post_author.update_reputation(self.ACCEPTED_ANSWER_SCORE)
            