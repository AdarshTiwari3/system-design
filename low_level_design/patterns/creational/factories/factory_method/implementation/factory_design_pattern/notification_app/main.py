'''main method for notification system app or client method'''

from factories.slack_notification_creator import SlackNotificationCreator
from factories.sms_notification_creator import SMSNotificationCreator
from factories.email_notification_creator import EmailNotificationCreator


def run_notification_system():
    print("\nImplementation of app is here")

    print("\nsend a slack notification")
    notify_slack=SlackNotificationCreator()
    notify_slack.send_notification()
    
    print("\nsend a sms notification to the user")
    notify_sms=SMSNotificationCreator()
    notify_sms.send_notification()
    
    print("\nsend an email to the user")
    notify_email=EmailNotificationCreator()
    notify_email.send_notification()



if __name__ == "__main__":
    print("\nImplementing notification system using factory method")
    run_notification_system()