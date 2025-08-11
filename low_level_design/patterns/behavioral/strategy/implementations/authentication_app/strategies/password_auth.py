"""Concrete strategy implementing password-based authentication."""

import time
from interfaces.auth_strategy import AuthStrategy


class PasswordAuthStrategy(AuthStrategy):
    """Authenticate users via username-password validation."""

    def authenticate(self, user_data: dict[str, str]) -> bool:
        """
        Authenticate user using password strategy.

        Args:
            user_data (dict): Must contain 'username' and 'password'.

        Returns:
            bool: True if authentication succeeds, else False.
        """
        username = user_data.get("username")
        password = user_data.get("password")

        if not username or not password:
            print("❌ Missing credentials.")
            return False

        print("\nPlease wait... verifying user details via password authentication strategy")
        time.sleep(1)  # Simulate delay

        if username == "admin" and password == "1234":
            print("\n✅ Verified user successfully")
            return True

        print("❌ Forbidden, 403 - Not authorized user")
        return False
