#code practice

# Single Responsibility Principle - each class will have single responsibilty

class UserAuthentication:
    def authenticate_user(self,username,password):
         print(f"Authenticating user '{username}' with provided password...")

class UserProfileManager:
    def update_user_profile(self,user_id,new_profile):
        print(f"Updating profile for user ID {user_id} with data: {new_profile}")

class EmailNotifier:
    def send_email_notification(self,user_name,user_email,msg):
        print(f"Sending email to {user_email} (User: {user_name}) with message: '{msg}'")


# Create objects
def single_responsibility_fun():
    auth = UserAuthentication()
    profile_mgr = UserProfileManager()
    notifier = EmailNotifier()

    # Call methods with better arguments
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
