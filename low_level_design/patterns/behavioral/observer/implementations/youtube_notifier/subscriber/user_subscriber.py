"""subscribed user for youtube channel , they will get the updates from the youtube channel(publisher) when some event gets triggered"""

from subscriber.subscriber_interface import SubscriberInterface

class UserSubscriber(SubscriberInterface):
    """Subscribed user for youtube channel"""
    def __init__(self, name: str):
        self.__name=name

    def update(self, message: str) -> None:
        """Receive a notification from publisher"""

        print(f"\n[Notification]-📧 {self.__name} got notification message- {message}")
    
    
    @property
    def name(self) -> str:
        return self.__name