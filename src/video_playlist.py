"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self):
        self._playlists = {}      # name of playlist as key and list of videos as value

    def playlist_exist(self, name: str) -> bool:
        """Returns `True` if a playlist already exist"""

        playlists = [i.lower() for i in self._playlists.keys()]

        return name.lower() in playlists

    def add_playlist(self, name: str):
        """Creates a new playlist with the name `name`"""

        if not self.playlist_exist(name):
            self._playlists[name] = []
            print(f"Successfully created new playlist: {name}")
        else:
            print("Cannot create playlist: A playlist with the same name already exists")