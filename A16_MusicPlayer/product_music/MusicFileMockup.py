from product_music.Musikstueck import Musikstueck


class MusicFileMockup(Musikstueck):

    def abspielen(self):
        """
        Mockup-class that only gives out the information of the test songs and do not play them

        :return: None
        """
        print("Current song: %s, Interpret: %s, Album: %s" % (self.titel, self.interpret, self.album))
