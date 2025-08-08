"""Publisher (Subject/Observable) interface.
Responsible for managing subscribers and tracking events or state changes
that will trigger notifications to all registered subscribers."""


from abc import ABC, abstractmethod
from subscriber.subscriber_interface import SubscriberInterface

class PublisherInterface(ABC):
    @abstractmethod
    def add_observer(self, observer: SubscriberInterface) -> None:
        """Register an observer to receive notifications."""
        pass

    @abstractmethod
    def remove_observer(self, observer: SubscriberInterface) -> None:
        """Unregister an observer so it no longer receives notifications."""
        pass

    @abstractmethod
    def notify_observers(self, message: str) -> None:
        """Notify all registered observers about an event or state change."""
        pass