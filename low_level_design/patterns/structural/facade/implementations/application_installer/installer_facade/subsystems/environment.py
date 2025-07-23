import time
class EnvironmentSetup:
    """subsystem to setup the environment variables"""
    def set_environment(self) -> None:
        print("\n[ENV] setting up environment variables...")
        self._simulate_delay()
        print("\n✓ all set here you go")
    def _simulate_delay(self) -> None:
        time.sleep(5)