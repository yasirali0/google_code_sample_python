"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist

import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = None     # to know which video is being played
        self._video_playlist = Playlist()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        
        # dict with `title` as the key for sorting purpose
        all_videos = {}

        print("Here's a list of all available videos:")
        
        # iterate over the keys i.e `video_id` of `_videos` dict in `_video_library`
        for video_id in self._video_library._videos.keys():
            
            # get the `video` object for the `video_id`
            video = self._video_library.get_video(video_id)
            
            # get the properties
            title = video.title 
            id = video.video_id
            tags = " ".join(video.tags)
            
            all_videos[title] = f"{title} ({id}) [{tags}]"
        
        # sort lexicographically by title
        for video in sorted(all_videos.keys()):
            print(all_videos[video])

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        video = self._video_library.get_video(video_id)
        
        if video is not None:
            if self._current_video is None:
                print(f"Playing video: {video.title}")
                self._current_video = video
            else:
                self._current_video.pause(False)         # set the pause status to False
                print(f"Stopping video: {self._current_video.title}")
                print(f"Playing video: {video.title}")
                self._current_video = video

        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""

        if self._current_video is None:
            print("Cannot stop video: No video is currently playing")
        else:
            print(f"Stopping video: {self._current_video.title}")
            self._current_video = None

    def play_random_video(self):
        """Plays a random video from the video library."""

        videos = self._video_library.get_all_videos()
        
        if len(videos) != 0:
            #select at random from the `videos` list
            rand_video = random.choice(videos)

            # if a video is running, stop it
            if self._current_video is not None:
                print(f"Stopping video: {self._current_video.title}")

            # play a random video
            print(f"Playing video: {rand_video.title}")
            self._current_video = rand_video
        
        # in case no videos are available
        else:
            print("No videos available")

    def pause_video(self):
        """Pauses the current video."""

        if self._current_video is not None:
            if not self._current_video._paused:
                print(f"Pausing video: {self._current_video.title}")
                self._current_video.pause()         # set pause status to True - Default argumnet is True
            else:
                print(f"Video already paused: {self._current_video.title}")
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        if self._current_video is not None:
            if self._current_video._paused:
                print(f"Continuing video: {self._current_video.title}")
                self._current_video.pause(False)
            else:
                print("Cannot continue video: Video is not paused")

        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""

        if self._current_video is not None:
            title = self._current_video.title
            id = self._current_video.video_id
            tags = " ".join(self._current_video.tags)
            pause_status = self._current_video.pause_status

            print(f"Currently playing: {title} ({id}) [{tags}] {pause_status}")
        
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        self._video_playlist.add_playlist(playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if self._video_playlist.playlist_exist(playlist_name):
            video = self._video_library.get_video(video_id)
            if video is not None:
                if video not in self._video_playlist._playlists.setdefault(playlist_name, []):
                    self._video_playlist._playlists.setdefault(playlist_name, []).append(video)
                    print(f"Added video to {playlist_name}: {video.title}")
                else:
                    print(f"Cannot add video to {playlist_name}: Video already added")
            else:
                print(f"Cannot add video to {playlist_name}: Video does not exist")
        else:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")

    def show_all_playlists(self):
        """Display all playlists."""

        # all_playlists = self._video_playlist._playlists.keys()
        # print(all_playlists)
        pass

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
