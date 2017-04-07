import argparse
import os
import sys
import inspect
from source import engines


class DoZip:

    def __init__(self, dest, source, archive_engine, name):
        """
        Constructor of the do_py class
        It makes a dictionary that contains every type of the different engines classes
        Than it checks if the destination is available and if the source is available
        And if the input archive engine is correct
        Then it calls the class and sets the source
        It also prints the description

        :param dest: The destination of the archive
        :param source: The source of the archive
        :param archive_engine: The used engine
        :param name: The name of the .zip/.tar file
        """
        engines_dict = self.read_engines()
        try:
            if archive_engine in engines_dict:
                used_engine = engines_dict[archive_engine](name, dest)
                used_engine.set_filelist(source)
                print(used_engine)
                used_engine.write()
            else:
                print("Wrong engine")
        except (FileNotFoundError, FileExistsError):
            print("Wrong source or destination")

    @staticmethod
    def read_engines():
        """
        Reads the module engines out and puts the names and object of the classes in a dictionary
        Help from:
        http://stackoverflow.com/questions/5520580/how-do-you-get-all-classes-defined-in-a-module-but-not-imported

        :return: A dictionary with the names and objects of an module
        """
        engines_dict = {}
        md = engines.__dict__
        engines_arr = [md[c] for c in md if (isinstance(md[c], type) and md[c].__module__ == engines.__name__)]
        for class_type in engines_arr:
            class_name = class_type.__name__[:3] + "_" + class_type.__name__[3:]
            engines_dict[class_name.upper()] = class_type
        return engines_dict

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    curr_path = os.getcwd()
    poss_engines = " ".join(str(x) for x in DoZip.read_engines().keys())
    dest = parser.add_argument('-d', '--dest-dir',
                               help='Output destination directory (default=Current Working Directory)',
                               default=curr_path)
    source = parser.add_argument('-s', '--src-dir',
                                 help='Input root directory (default=Current Working Directory)',
                                 default=curr_path)
    archive_engine = parser.add_argument('-a', '--archive-engine',
                                         help='Use the given archive engine (default=ZIP_STORED)\n'
                                              'Possible engines: ' + poss_engines,
                                         default="ZIP_STORED")
    name = parser.add_argument('-n', '--archive-name',
                               help='Name of the archive (default=archive)',
                               default="archive")
    args = parser.parse_args()
    client = DoZip(args.dest_dir, args.src_dir, args.archive_engine, args.archive_name)
