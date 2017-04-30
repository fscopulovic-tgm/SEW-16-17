from factory_musicdb.MusikdatenbankFabrik import MusikdatenbankFabrik
from product_music.MusicFileMockup import MusicFileMockup


class MusicMockupDB(MusikdatenbankFabrik):
    def __init__(self):
        """
        This is the constructor of the MusicMockupDB class
        It just calls the constructor of the super class and makes a list that contain the test songs
        """
        MusikdatenbankFabrik.__init__(self)
        self.playlist = []

    def lade_musik(self):
        """
        Puts the test songs in the playlist list and it calls the constructor of the MusicFileMockup class to add the
        songs

        :return: None
        """
        self.playlist.append(MusicFileMockup("Test 1", "Filip", "Loves Factory pattern"))
        self.playlist.append(MusicFileMockup("Test 2", "Filip", "Loves Factory pattern"))
