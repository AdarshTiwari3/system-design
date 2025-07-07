'''concreate class of notification abstract class'''

from models.notification import Notification

class SlackNotification(Notification):
    def send(self):
        print("Sending slack notification...")