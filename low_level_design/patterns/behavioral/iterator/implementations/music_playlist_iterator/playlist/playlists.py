from interfaces.iterable_collection_interface import IterableCollectionInterface
from interfaces.iterator_interface import IteratorInterface
from models.songs import Songs
from playlist.playlist_iterator import PlaylistIterator


class Playlist(IterableCollectionInterface):
    def __init__(self, name: str) -> None:
        """playlist will have name and list of songs"""
        self.name=name
        self._songs: list[Songs]=[]

    def add_song(self, song: Songs):
        if song not in self._songs:
            self._songs.append(song)
           

    def get_songs(self) -> list:
        return self._songs.copy()
    
    def remove_song(self, song: Songs):
        if song in self._songs:
            self._songs.remove(song)

    def get_iterator(self) -> IteratorInterface:
        return PlaylistIterator(self.get_songs())