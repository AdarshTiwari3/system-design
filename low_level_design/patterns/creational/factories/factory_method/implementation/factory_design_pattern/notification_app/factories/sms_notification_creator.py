'''
sms concreate creator

'''
from models.notification import Notification
from factories.notification_creator import NotificationCreator
from models.sms_notification import SMSNotification

class SMSNotificationCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return SMSNotification()