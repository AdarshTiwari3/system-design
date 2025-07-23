"""Installer facade, here facade will call internally each subsystem to hide the complexity of system from client"""
from installer_facade.subsystems import *
from typing import Optional

class ApplicationInstaller: #Installer Facade as client will consume this only
    """
        Facade class that provides a simplified interface for installing the application.
        Internally orchestrates all subsystems like environment setup, file copying,
        dependency installation, and shortcut creation.
    """
    def __init__(self,env: Optional[EnvironmentSetup] = None,files: Optional[FileManager] = None,deps: Optional[DependencyManager] = None,shortcuts: Optional[ShortcutCreator] = None):
        #using private variables as we don't want to show internal implmentation to achieve abstraction
        self.__env = env or EnvironmentSetup()
        self.__files = files or FileManager()
        self.__deps = deps or DependencyManager()
        self.__shortcuts = shortcuts or ShortcutCreator()

    def install(self) -> None:
        print("\nStarting installation...\n")
        self.__env.set_environment()
        self.__files.copy_files()
        self.__deps.install_dependencies()
        self.__shortcuts.create_shortcuts()
        print("\n✅Installation completed successfully✅!")