"""songs implementation of music playlist"""

class Songs:
    def __init__(self, title: str, artist: str) -> None:
        self._title=title
        self._artist=artist

    def play(self):
        print(f"🎵 Playing: {self._title} by {self._artist}")

    def __str__(self) -> str:
        return f"{self._title}-{self._artist}"