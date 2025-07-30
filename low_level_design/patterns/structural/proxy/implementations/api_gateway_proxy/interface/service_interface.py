"""Interface for API Gateway service"""
from abc import ABC, abstractmethod

class ServiceInterface(ABC):
    @abstractmethod
    def handle_request(self, request: dict) -> str:
        pass