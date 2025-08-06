from interfaces.iterator_interface import IteratorInterface

from models.songs import Songs

class PlaylistIterator(IteratorInterface):
    def __init__(self,  songs: list[Songs]) -> None:
        self._songs=songs
        self._index=0


    def has_next(self) -> bool:
        return self._index < len(self._songs)-1
    
    def next(self): # type: ignore
        if self.has_next():
            self._index += 1
            return self._songs[self._index]
        return None
    
    def has_previous(self) -> bool:
        return self._index > 0
    
    def previous(self): # type: ignore
        if self.has_previous():
            self._index -= 1
            return self._songs[self._index]
        return None
    
    def current(self): # type: ignore
        return self._songs[self._index]