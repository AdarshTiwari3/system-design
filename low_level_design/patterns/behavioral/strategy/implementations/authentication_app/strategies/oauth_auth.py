"""Concrete implementation of OAuth authentication strategy."""
import time
from interfaces.auth_strategy import AuthStrategy


class OAuthStrategy(AuthStrategy):
    def authenticate(self, user_data: dict[str, str]) -> bool:
        """Authenticate user using OAuth token."""
        auth_provider = user_data.get("auth_provider")
        token = user_data.get("token")

        print("\nPlease wait... verifying the OAuth details via OAuth Strategy")
        time.sleep(2)

        # Simulate OAuth validation
        if token == "valid_oauth_token":
            print("✅ Verified user successfully")
            return True
        
        print("❌ Forbidden, 403 - Not authorized user")
        return False
