from factory_musicdb.MusikdatenbankFabrik import MusikdatenbankFabrik
from product_music.MusicFile import MusicFile
import os
import pyglet
from mutagen.mp3 import MP3


class MusicDB(MusikdatenbankFabrik):
    def __init__(self, playlist_path):
        """
        This is the constructor of the MusicDB class
        The class inheritance from MusikdatenbankFabrik
        First it calls the superclass constructor
        then it makes a list called playlist where the music files are stored
        and it saves the path of the music folder as playlist_dir

        :param playlist_path: Path where the music is
        """
        MusikdatenbankFabrik.__init__(self)
        self.playlist = []
        self.playlist_dir = playlist_path

    def lade_musik(self):
        """
        This method is from the super class
        It goes through the whole files from the path
        It adds the music file to the pyglet media
        Gets the info of the music file and at the end it makes a new MusicFile object with the whole info

        :return: None
        """
        for dirname, foldername, files in os.walk(self.playlist_dir):
            for file in files:
                file_path = dirname + os.path.sep + file
                music_file = pyglet.media.load(file_path)
                info = MP3(file_path)

                s_length = info.info.length
                s_title = info["TIT2"]
                s_interpret = info["TPE1"]
                s_album = info["TALB"]

                self.playlist.append(MusicFile(music_file, s_length, s_title, s_interpret, s_album))
