"""Subscriber (Observer) interface.
Defines the method(s) to be implemented by any class that wants to receive 
notifications from the Publisher when a specific event or state change occurs."""


from abc import ABC, abstractmethod

class SubscriberInterface(ABC):
    """Subscriber (Observer) interface.
    Defines the contract for receiving event notifications from a Publisher.
    """

    @abstractmethod
    def update(self, message: str) -> None:

        """Receive a notification from the Publisher with relevant message or data."""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass