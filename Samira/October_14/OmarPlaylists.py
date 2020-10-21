from functools import lru_cache


class Solution:
    MAX = 10 ** 9 + 7

    @lru_cache(None)
    def playlist_of_size(self, size, num_songs):
        if size == 0:
            return +(num_songs == 0)
        out = self.playlist_of_size(size - 1, num_songs) * max(num_songs - self.min_times, 0)
        out += self.playlist_of_size(size - 1, num_songs - 1) * (self.total_songs - num_songs + 1)
        return out % self.MAX

    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        # N = num unique songs
        # L = total songs to play
        # K = limit before songs can repeat

        self.total_songs = N
        self.playlist_length = L
        self.min_times = K

        return self.playlist_of_size(self.playlist_length, self.total_songs)
