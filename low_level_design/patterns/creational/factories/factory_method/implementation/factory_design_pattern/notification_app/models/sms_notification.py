'''concreate class'''

from models.notification import Notification

class SMSNotification(Notification):
    def send(self):
        print("sending sms to the user...")