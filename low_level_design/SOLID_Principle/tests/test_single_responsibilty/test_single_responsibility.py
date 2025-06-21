import typing
import pytest
from low_level_design.SOLID_Principle.single_responsibility.single_responsibility import (
    EmailNotifier,
    UserAuthentication,
    UserProfileManager
)

"""
Command to run:
    PYTHONPATH=$(pwd) pytest low_level_design/SOLID_Principle/tests/
OR
    Configure pytest.ini in root directory:
    [pytest]
    pythonpath = .
"""

def test_authenticate_user(capfd) -> None:
    """Test that the user authentication prints correct output"""
    auth = UserAuthentication()
    username: str = "Rhon"
    password: str = "RohnPassword"
    auth.authenticate_user(username, password)

    output, _ = capfd.readouterr()
    expected_output = "Authenticating user 'Rhon' with provided password..."

    assert expected_output in output, f"\nExpected output: '{expected_output}\n', but got: '{output}'"

def test_email_notifier(capfd) -> None:
    """Test that the email notifier prints the correct output"""
    notifier = EmailNotifier()
    user_name: str = "Andy"
    user_email: str = "andy@mail.com"
    msg: str = "your address changed successfully"

    notifier.send_email_notification(user_name, user_email , msg )

    output, _ = capfd.readouterr()
    expected_output = "Sending email to andy@mail.com (User: Andy) with message: 'your address changed successfully'"

    assert expected_output in output, f"\nExpected output: '{expected_output}\n', but got: '{output}'"

def test_user_profile_manager(capfd) -> None:
    """Test that the user profile manager prints the correct output"""
    manager = UserProfileManager()
    
    user_id: int = 102

    data: dict[str, str] = {'name': 'Andy Joe', 'Address': 'America'}

    manager.update_user_profile(user_id, data)

    output, _ = capfd.readouterr()
    expected_output = f"Updating profile for user ID {user_id} with data: {data}"

    assert expected_output in output, f"\nExpected output: '{expected_output}\n', but got: '{output}'"
