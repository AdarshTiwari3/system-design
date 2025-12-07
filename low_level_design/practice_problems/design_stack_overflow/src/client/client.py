"""Stack Overflow Client runner- main function"""
from facade.stackoverlow_facade import StackOverflowFacade
from entities import Tag, User
from strategies import *
from enums import VoteType
from typing import Set, List

class StackOverflowClient:
    def __init__(self):
        self.stackoverflow_facade=StackOverflowFacade()


    def create_users(self) -> User:
        johndoe=self.stackoverflow_facade.create_user("John Doe")
        smith=self.stackoverflow_facade.create_user("Alex Smith")
        hyper_xoxo=self.stackoverflow_facade.create_user("Hyper Xoxo Royan")
        return johndoe, smith, hyper_xoxo

    def create_tags(self) -> Set[Tag]:
        python=Tag("Python")
        system_design=Tag("System Design")
        lld=Tag("LLD")
        stack_overflow= Tag("Stack Overflow Problem")
        tags={python, system_design, lld, stack_overflow} #set to avoid any duplicates
        return tags
    
    @staticmethod
    def display_reputation(users: List[User]):
        print("------Reputation------")
        for user in users:
            print(f"{user.get_username()}: {user.get_reputation()}")

    def main(self):

        #create users
        john,smith,xoxo=self.create_users() 

        #create tags
        tags=self.create_tags()

        # post a question
        question = self.stackoverflow_facade.post_question(
            john.get_user_id(),
            "How to implement Observer Pattern?",
            "I want to understand how to implement Observer pattern in Python...",
            tags
        )

        # post answers
        answer1 = self.stackoverflow_facade.post_answer(
            smith.get_user_id(),
            question.get_content_id(),
            "You can implement it using the Observer base class."
        )

        answer2 = self.stackoverflow_facade.post_answer(
            xoxo.get_user_id(),
            question.get_content_id(),
            "Consider using the Observer pattern with callback functions."
        )

        # votes (all positive here)
        self.stackoverflow_facade.vote_on_post(
            john.get_user_id(),
            answer1.get_content_id(),
            VoteType.UPVOTE
        )
        self.stackoverflow_facade.vote_on_post(
            smith.get_user_id(),
            answer2.get_content_id(),
            VoteType.UPVOTE
        )
        self.stackoverflow_facade.vote_on_post(
            xoxo.get_user_id(),
            question.get_content_id(),
            VoteType.UPVOTE
        )

        # accept an answer
        self.stackoverflow_facade.accept_answer(
            question.get_content_id(),
            answer1.get_content_id()
        )

        # second question by John, also Python-related
        python_and_lld_tags = {tag for tag in tags if tag.get_tag_name() in ("Python", "LLD")}
        question2 = self.stackoverflow_facade.post_question(
            john.get_user_id(),
            "Best practices for LLD in Python?",
            "What are some patterns and best practices for designing LLD in Python?",
            python_and_lld_tags
        )
        # more answers
        answer3 = self.stackoverflow_facade.post_answer(
            smith.get_user_id(),
            question2.get_content_id(),
            "Start with clear requirements and use SOLID principles."
        )

        answer4 = self.stackoverflow_facade.post_answer(
            xoxo.get_user_id(),
            question2.get_content_id(),
            "Use design patterns like Factory, Strategy, and Observer where appropriate."
        )
        # John upvotes his own question2 (depending on your rules, may or may not be rewarded)
        self.stackoverflow_facade.vote_on_post(
            john.get_user_id(),
            question2.get_content_id(),
            VoteType.UPVOTE
        )

        # Xoxo downvotes question2
        self.stackoverflow_facade.vote_on_post(
            xoxo.get_user_id(),
            question2.get_content_id(),
            VoteType.DOWNVOTE
        )
        # John downvotes Smith's answer3
        self.stackoverflow_facade.vote_on_post(
            john.get_user_id(),
            answer3.get_content_id(),
            VoteType.DOWNVOTE
        )

        # Smith upvotes his own answer3 (again, rule depends on your reputation manager)
        self.stackoverflow_facade.vote_on_post(
            smith.get_user_id(),
            answer3.get_content_id(),
            VoteType.UPVOTE
        )

        # Both John and Smith upvote Xoxo's answer4
        self.stackoverflow_facade.vote_on_post(
            john.get_user_id(),
            answer4.get_content_id(),
            VoteType.UPVOTE
        )
        self.stackoverflow_facade.vote_on_post(
            smith.get_user_id(),
            answer4.get_content_id(),
            VoteType.UPVOTE
        )

        # Accept a different answer for question2
        self.stackoverflow_facade.accept_answer(
            question2.get_content_id(),
            answer4.get_content_id()
        )
        
        print("------Votes------")
        print(f"Question 1: '{question.get_title()}' -> votes: {question.get_vote_count()}")
        print(f"Answer 1 (by {smith.get_username()}) -> votes: {answer1.get_vote_count()}")
        print(f"Answer 2 (by {xoxo.get_username()}) -> votes: {answer2.get_vote_count()}")
        print()
        print(f"Question 2: '{question2.get_title()}' -> votes: {question2.get_vote_count()}")
        print(f"Answer 3 (by {smith.get_username()}) -> votes: {answer3.get_vote_count()}")
        print(f"Answer 4 (by {xoxo.get_username()}) -> votes: {answer4.get_vote_count()}")
        print()

        # Show reputation summary (Observer/Events should have updated this)
        self.display_reputation([john, smith, xoxo])
        print()

        python_tag = next(tag for tag in tags if tag.get_tag_name() == "Python")  # next item from an iterator.
        strategies = [UserSearchStrategy(john), TagSearchStrategy(python_tag)]

        search_results = self.stackoverflow_facade.search_questions(strategies)

        print("------Search Results------")
        if not search_results:
            print("No questions found for the given strategies.")
        else:
            for q in search_results:
                author = q.get_content_author().get_username()
                tags_for_q = q.get_all_tags()
                tag_names = [t.get_tag_name() for t in tags_for_q]
                answers = q.get_all_answers()

                print(f"Question: {q.get_title()}")
                print(f"Question ID: {q.get_content_id()}")
                print(f"Title     : {q.get_title()}")
                print(f"Author    : {author}")
                print(f"Votes     : {q.get_vote_count()}")
                print(f"Tags      : {', '.join(tag_names) if tag_names else 'N/A'}")
                print(f"Answers   : {len(answers)}")
                print("-" * 50)

        print()