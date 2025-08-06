from playlist.playlists import Playlist
from models.songs import Songs

def run_playlist():
    playlist=Playlist("Workout Songs")
    #Adding songs to playlist
    
    playlist.add_song(Songs("Malang", "Ved Sharma"))
    playlist.add_song(Songs("Apna Time Aayega", "Ranveer Singh"))
    playlist.add_song(Songs("Kar Har Maidaan Fateh", "Sukhwinder Singh"))
    playlist.add_song(Songs("Brothers Anthem", "Vishal Dadlani"))


    iterator=playlist.get_iterator()

    print(f"\n🎧 playing the song from playlist: {playlist.name}\n")

    current_song=iterator.current()
    current_song.play() # type: ignore

    while iterator.has_next():
        next_song=iterator.next()
        next_song.play() # type: ignore


