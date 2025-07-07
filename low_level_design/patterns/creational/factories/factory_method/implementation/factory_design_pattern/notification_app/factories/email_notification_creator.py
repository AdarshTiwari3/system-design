'''email concreate creator of NotificationCreator class'''
from models.notification import Notification
from models.email_notification import EmailNotification
from factories.notification_creator import NotificationCreator

class EmailNotificationCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return EmailNotification()