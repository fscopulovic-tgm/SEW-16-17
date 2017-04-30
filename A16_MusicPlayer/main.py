from factory_musicdb.MusicDB import *
from factory_musicdb.MusicMockupDB import *
import argparse
import os
__author__ = 'DD'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    curr_path = os.getcwd()
    source_path = parser.add_argument('-s', '--src-dir',
                                      help='Source of the playlist (default=Current Working Directory)',
                                      default=curr_path)
    args = parser.parse_args()
    fabrik = MusicDB(args.src_dir)
    #fabrik = MusicMockupDB()
    fabrik.abspielen()
