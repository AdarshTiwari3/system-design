"""Stack Overflow Facade- this will be consumed by client"""
from entities import User, Question, Answer, Post, Tag
from observer import ReputationScoreManager
from enums import VoteType
from strategies import SearchStrategy

from typing import Dict, Set, List, Optional
import threading

class StackOverflowFacade:
    def __init__(self):
        self.users: Dict[str, User]={}
        self.questions: Dict[str, Question]={}
        self.answers: Dict[str, Answer]={}
        self.reputation_manager = ReputationScoreManager()
        self._lock = threading.Lock()

    def create_user(self, username: str) -> User:
        with self._lock:
            user = User(username)
            self.users[user.get_user_id()] = user
            return user

    
    def remove_user(self, user: User) -> Optional[User]:
        with self._lock:
            return self.users.pop(user.get_user_id(), None)

    def get_users_list(self) -> Dict[str, User]:
        with self._lock:
            return dict(self.users)
    
    def get_user(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)

    def post_question(self, user_id: str, title: str, body: str, tags: Set[Tag]) -> Question:
        with self._lock:
            if user_id not in self.users:
                raise KeyError("User not found")

            author = self.users[user_id]
            question = Question(title, body, author, tags)
            question.add_observer(self.reputation_manager)

            self.questions[question.get_content_id()] = question

            return question

    
    def post_answer(self, user_id: str, question_id: str, body: str) -> Answer:
        with self._lock:
            if user_id not in self.users:
                raise KeyError("User not found")
            if question_id not in self.questions:
                raise KeyError("Question not found")

            author = self.users[user_id]
            question = self.questions[question_id]

            answer = Answer(body, author)
            answer.add_observer(self.reputation_manager)

            question.add_answer(answer)
            self.answers[answer.get_content_id()] = answer

            return answer
    
    def vote_on_post(self, user_id: str, post_id: str, vote_type: VoteType):
        with self._lock:
            if user_id not in self.users:
                raise KeyError("User not found")

            user = self.users[user_id]
            post = self.find_post_by_id(post_id)

            post.vote(user, vote_type)



    def find_post_by_id(self, post_id: str) -> Post:
        if post_id in self.questions:
            return self.questions[post_id]
        if post_id in self.answers:
            return self.answers[post_id]
        raise KeyError("Post not found")



    def accept_answer(self, question_id: str, answer_id:str):
        with self._lock:
            if question_id not in self.questions:
                raise KeyError("Question not found")
            if answer_id not in self.answers:
                raise KeyError("Answer not found")
            
            question=self.questions[question_id]
            answer=self.answers[answer_id]
            question.accept_answer(answer)

    def search_questions(self, strategies:  Optional[List[SearchStrategy]] = None,) -> List[Question]:
        """
        Apply search strategies sequentially to filter questions.
        Returns list of matching questions.
        """
        all_questions = list(self.questions.values())
        result_set = set()
        for strategy in strategies:
            for q in strategy.search(all_questions):
                result_set.add(q)
        return list(result_set)