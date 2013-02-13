"""MusicAPI by Jurriaan Bremer.

Copyright (C) 2013 Jurriaan Bremer

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import sys


class Track:
    def __init__(self, track_id=None):
        self.track_id = track_id

    def play(self):
        """Play this track."""

    def album(self):
        """Album of this track."""

    def artist(self):
        """Artist of this track."""

    def duration(self):
        """Duration of this track."""

    def genre(self):
        """Genre of this track."""

    def name(self):
        """Name of this track."""

    def playcount(self):
        """Played count of this track."""

    def rating(self):
        """Rating of this track."""

    def year(self):
        """Year of this track."""


class Playlist:
    def __init__(self, playlist_id=None):
        self.playlist_id = playlist_id

    def tracks(self):
        """Returns a list of all Tracks."""


class Instance:
    def play(self):
        """Play the currently targeted track."""

    def stop(self):
        """Stop the currently playing song."""

    def pause(self):
        """Pause the currently playing song."""

    def toggle(self):
        """Toggle between Playing and Paused."""

    def resume(self):
        """Resume the currently paused song."""

    def next(self):
        """Skip to the next song."""

    def prev(self):
        """Go back to the previous song."""

    def volume(self, new_volume=None):
        """Volume in the range 0..100."""

    def mute(self, is_mutex):
        """Mutes or un-mutes the player."""

    def progress(self):
        """Gets the progress of the song, returns (position, length)."""

    def current_song(self):
        """Current song that's playing."""

    def current_playlist(self):
        """Current playlist that's playing."""


def instance(program):
    if program == 'iTunes':
        if sys.platform == 'win32':
            import itunes_win32
            return itunes_win32.Instance()
