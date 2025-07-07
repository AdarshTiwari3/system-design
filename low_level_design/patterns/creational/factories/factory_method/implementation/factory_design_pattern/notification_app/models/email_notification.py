'''email product concreate class of notification'''
from models.notification import Notification

class EmailNotification(Notification):
    def send(self):
        print("sending email notification...")