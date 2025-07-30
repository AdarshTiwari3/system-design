"""UserService concrete class that handles user-specific operations."""

from interface.service_interface import ServiceInterface

class UserService(ServiceInterface):
    def handle_request(self, request: dict) -> str:
        
        user_id = request.get("user_id")

        if user_id is None:
            return "[UserService] Error: user_id not provided"

        
        return f"[UserService] has been called and your user ID is: {user_id}"