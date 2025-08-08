"""Youtube channel publisher which will notify its subscriber/ observer if some event occurs or video gets uploaded"""

from publisher.publisher_interface import PublisherInterface
from subscriber.subscriber_interface import SubscriberInterface
class YoutubeChannelPublisher(PublisherInterface):
    def __init__(self, channel_name: str):
        # this holds the list of subscribers
        self.__channel_name=channel_name
        self.__subscribers: list[SubscriberInterface]=[]


    def add_observer(self, observer: SubscriberInterface) -> None:
        """Register an observer."""
        if observer in self.__subscribers:
            raise ValueError(f"Subscriber '{observer.name}' is already subscribed to '{self.__channel_name}'.")
               
        self.__subscribers.append(observer)
        print(f"[INFO]- 🙍 {observer.name} subscribed to the channel: {self.__channel_name} ") # type: ignore

    def remove_observer(self, observer: SubscriberInterface) -> None:
        """Unregister an observer."""
        if observer in self.__subscribers:
            self.__subscribers.remove(observer)
            print(f"[INFO]- 🙍 {observer.name} unsubscribed the channel: {self.__channel_name} ") # type: ignore
        else:
            print(f"⚠️ Cannot remove '{observer.name}' — not subscribed.") # type: ignore

    def add_video(self, video_title: str) -> None:
        """
        Simulate adding a new video to the channel and notify subscribers.

        Args:
            video_title (str): The title of the uploaded video.
        """
        print("[INFO] Video stored and fetched from DB successfully.")
        message = f"🎬 New video '{video_title}' uploaded on channel: {self.__channel_name}"
        self.notify_observers(message)


    def notify_observers(self, message: str) -> None:
       
        """Send a message to all subscribers."""
        print(f"[PUBLISHER]🖥️ - {self.__channel_name}: {message}")

        """Notify all the subscriber as some event has been triggered"""

        for subscriber in self.__subscribers:
            subscriber.update(message)
