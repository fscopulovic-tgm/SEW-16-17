import argparse
import os
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
        engines_dict = {
            "ZIP_STORED": engines.ZipWithoutCompression,
            "ZIP_LZMA": engines.ZipWithLZMACompression,
            "ZIP_BZIP2": engines.ZipWithBZIP2Compression,
            "ZIP_DEFLATED": engines.ZipWithDeflatedCompression,
            "TAR_GZIP": engines.TarWithGZIPCompression,
            "TAR_STORED": engines.TarWithoutCompression,
            "TAR_LZMA": engines.TarWithLZMACompression,
            "TAR_BZIP2": engines.TarWithBZIP2Compression
        }
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    curr_path = os.getcwd()
    print(curr_path)
    dest = parser.add_argument('-d', '--dest-dir',
                               help='Output destination directory (default=Current Working Directory)',
                               default=curr_path)
    source = parser.add_argument('-s', '--src-dir',
                                 help='Input root directory (default=Current Working Directory)',
                                 default=curr_path)
    archive_engine = parser.add_argument('-a', '--archive-engine',
                                         help='Use the given archive engine (default=ZIP_STORED)',
                                         default="ZIP_STORED")
    name = parser.add_argument('-n', '--archive-name',
                               help='Name of the archive (default=archive)',
                               default="archive")
    args = parser.parse_args()
    client = DoZip(args.dest_dir, args.src_dir, args.archive_engine, args.archive_name)
