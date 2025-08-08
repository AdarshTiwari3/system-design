"""Client code.
Responsible for creating Publisher and Subscriber instances,
registering subscribers with the publisher, and triggering events
to demonstrate or execute the Observer pattern in action."""


from publisher.youtube_channel_publisher import YoutubeChannelPublisher
from subscriber.user_subscriber import UserSubscriber

def run_youtube_notifier():
    print("\nRunning youtube notifier for Observer Design Pattern")

    channel=YoutubeChannelPublisher("system-design-youtube-channel")

    john=UserSubscriber("John")
    smith=UserSubscriber("Smith")
    ady=UserSubscriber("Ady")
    trump=UserSubscriber("Trump")
    

    """Adding user/ subscriber to channel"""
    channel.add_observer(john)
    channel.add_observer(smith)
    channel.add_observer(ady)
    channel.add_observer(trump)

    """Add Video and it will notify the subscriber by default"""

    channel.add_video("Observer Design Pattern- explanation/implementation")

    channel.notify_observers("Will be live in 10 minutes")

    channel.remove_observer(trump)