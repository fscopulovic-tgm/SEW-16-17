from product_music.MusicFileMockup import Musikstueck
import time


class MusicFile(Musikstueck):

    def __init__(self, file, length, title, interpret, album):
        """
        Constructor of the MusicFile class
        It calls the constructor of the superclass and then it stores the file and the length

        :param file: The pyglet music file
        :param length: The length of the song
        :param title: The title of the song
        :param interpret: The interpret of the song
        :param album: The album of the song
        """
        Musikstueck.__init__(self, title, interpret, album)
        self.file = file
        self.length = length

    def abspielen(self):
        """
        This plays the music file
        It just calls the play method and prints out the info of the song
        It also makes a time.sleep with the length of the song
        Martin Woelfer helped me at this, because if you do not write the time.sleep it plays all songs at once

        :return: None
        """
        self.file.play()
        print("Current song: %s , Interpret: %s , Album: %s" % (self.title, self.interpret, self.album))
        time.sleep(self.length)
