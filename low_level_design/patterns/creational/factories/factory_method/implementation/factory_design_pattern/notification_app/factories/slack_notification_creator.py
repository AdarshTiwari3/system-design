'''
slack concreate creator subclass of notificationcreator parent class
'''

from models.notification import Notification
from factories.notification_creator import NotificationCreator
from models.slack_notification import SlackNotification

class SlackNotificationCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return SlackNotification()