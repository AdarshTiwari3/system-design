"""Actual implementation of proxy"""

from config.config import VALID_TOKENS
from interface.service_interface import ServiceInterface
class APIGatewayProxy(ServiceInterface):
    def __init__(self, real_service: ServiceInterface):
        self.__real_service=real_service

    def authentication(self, user_token: str) -> bool:
        return user_token in VALID_TOKENS
    
    def log(self, request: dict) -> None:
        print(f"[API Gateway] Request Log: {request}")

    def handle_request(self, request: dict) -> str:
        self.log(request)
        user_token=request.get("user_token")

        if not user_token and not self.authentication(user_token): # type: ignore
            return "[API Gateway] 403 Forbidden: Invalid Token"

        return self.__real_service.handle_request(request)