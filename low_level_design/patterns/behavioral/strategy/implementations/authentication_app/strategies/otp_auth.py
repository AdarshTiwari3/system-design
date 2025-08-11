"""Concrete implementation of OTP authentication strategy."""
import time
from interfaces.auth_strategy import AuthStrategy


class OTPAuthStrategy(AuthStrategy):
    def authenticate(self, user_data: dict[str, str]) -> bool:
        """Authenticate user using a one-time password (OTP)."""
        otp = user_data.get("otp")

        print("\nPlease wait... verifying the OTP via OTP Authentication Strategy")
        time.sleep(2)

        if otp == "234567":
            print("✅ OTP verified successfully")
            return True
        
        print("❌ Incorrect OTP, please try again")
        return False
