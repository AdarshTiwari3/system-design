"""
Subsystems for the Facade. The Facade will interact with these modules.
"""

from installer_facade.subsystems.dependency_manager import DependencyManager
from installer_facade.subsystems.environment import EnvironmentSetup
from installer_facade.subsystems.file_manager import FileManager
from installer_facade.subsystems.shortcuts_creator import ShortcutCreator

# __all__ defines the public API of this package when using: from subsystems import *
__all__ = [
    "DependencyManager",
    "EnvironmentSetup",
    "FileManager",
    "ShortcutCreator"
]

# Why strings?
# When `from subsystems import *` is used, Python looks at __all__.
# It uses each string (like "FileManager") to fetch the corresponding object 
# that has already been imported in this __init__.py file.
