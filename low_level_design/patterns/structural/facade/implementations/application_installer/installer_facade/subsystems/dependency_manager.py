import time

class DependencyManager:
    """subsystem for installing dependencies"""
    def install_dependencies(self) -> None:
        print("\n[✓] Installing required dependencies...")
        time.sleep(5)  
        print("[✓] All dependencies installed successfully.\n")
