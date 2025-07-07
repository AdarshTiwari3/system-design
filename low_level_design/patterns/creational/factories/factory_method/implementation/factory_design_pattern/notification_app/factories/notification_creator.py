'''notification creator, factory method'''

from abc import ABC, abstractmethod
from models.notification import Notification

class NotificationCreator(ABC):
    def send_notification(self) -> Notification:
        notification=self.create_notification()
        
        notification.send()

        return notification
    
    @abstractmethod
    def create_notification(self) -> Notification:
        pass #this will be factory method for notification creation this will be responsible for object creation and its subclass will implement this