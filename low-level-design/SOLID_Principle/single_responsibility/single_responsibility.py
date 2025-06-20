from typing import Dict

# Single Responsibility Principle - each class will have single responsibility

class UserAuthentication:
    def authenticate_user(self, username: str, password: str) -> None:
        print(f"Authenticating user '{username}' with provided password...")

class UserProfileManager:
    def update_user_profile(self, user_id: int, new_profile: Dict[str, str]) -> None:
        print(f"Updating profile for user ID {user_id} with data: {new_profile}")

class EmailNotifier:
    def send_email_notification(self, user_name: str, user_email: str, msg: str) -> None:
        print(f"Sending email to {user_email} (User: {user_name}) with message: '{msg}'")


# Create objects and call methods
def single_responsibility_fun() -> None:
    auth = UserAuthentication()
    profile_mgr = UserProfileManager()
    notifier = EmailNotifier()

    auth.authenticate_user("John", "Pa$$w0rd123")

    profile_mgr.update_user_profile(
        101,
        {
            "name": "John",
            "bio": "Adventurer, reader, and tea lover.",
            "location": "Wonderland"
        }
    )

    notifier.send_email_notification(
        "John",
        "John@example.com",
        "Your profile has been successfully updated!"
    )