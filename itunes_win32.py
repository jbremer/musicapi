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
from win32com.client import Dispatch
import musicapi

# global instance
instance = None


class Track(musicapi.Track):
    def __init__(self, track_id=None):
        musicapi.Track.__init__(self, track_id)
        self.data = instance.com.LibraryPlaylist.Tracks[track_id-1]

    def play(self):
        self.data.Play()

    def album(self):
        return self.data.Album

    def artist(self):
        return self.data.Artist

    def duration(self):
        return self.data.Duration

    def genre(self):
        return self.data.Genre

    def name(self):
        return self.data.Name

    def playcount(self):
        return self.data.PlayedCount

    def rating(self):
        return self.data.Rating

    def year(self):
        return self.data.Year


class Playlist(musicapi.Playlist):
    def __init__(self, playlist_id=None):
        musicapi.Playlist.__init__(self, playlist_id)

        # TODO support for other sources
        self.data = instance.com.Sources[0].Playlists[self.playlist_id-1]

    def tracks(self):
        for x in self.data.Tracks:
            yield Track(x.Index)


class Instance(musicapi.Instance):
    def __init__(self):
        """Initialize a Windows COM object to interact with iTunes."""
        global instance
        self.com = Dispatch('iTunes.Application')
        instance = self

    def play(self):
        self.com.Play()

    def stop(self):
        self.com.Stop()

    def pause(self):
        self.com.Pause()

    def toggle(self):
        self.com.PlayPause()

    def resume(self):
        self.com.Resume()

    def next(self):
        self.com.NextTrack()

    def prev(self):
        self.com.PreviousTrack()

    def volume(self, new_volume=None):
        if not new_volume is None:
            self.com.SoundVolume = int(new_volume)
        else:
            return self.com.SoundVolume

    def mute(self, is_muted):
        self.com.Mute = bool(is_muted)

    def progress(self):
        return self.com.PlayerPosition, self.com.CurrentTrack.Duration

    def current_song(self):
        track = self.com.CurrentTrack
        return Track(track.Index)

    def current_playlist(self):
        playlist = self.com.CurrentPlaylist
        return Playlist(playlist.Index)