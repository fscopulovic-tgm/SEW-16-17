import os
import tarfile
import zipfile

from source.engine import ArchiveEngine


class ZipWithoutCompression(ArchiveEngine):

    def write(self):
        """
        Writes a uncompressed .zip-file
        A lot of help from: http://stackoverflow.com/questions/14568647/create-zip-in-python

        :return: none
        """
        with zipfile.ZipFile(self.filename + ".zip", "w", zipfile.ZIP_STORED) as zipping:
            abs_src = os.path.abspath(self.source)
            for dir_name, sub_dirs, files in os.walk(self.source):
                for file in files:
                    abs_name = os.path.abspath(os.path.join(dir_name, file))
                    arc_name = abs_name[len(abs_src) + 1:]
                    zipping.write(abs_name, arc_name)

    def __str__(self):
        """
        Returns the description of the uncompressed zipfile

        :return: The description of the .zip file
        """
        return ">>Zipfile without compression\n>>Creates a .zip-file with the taken components"


class ZipWithLZMACompression(ArchiveEngine):

    def write(self):
        """
        Writes a LZMA-compressed .7z-file
        A lot of help from: http://stackoverflow.com/questions/14568647/create-zip-in-python

        :return: none
        """
        with zipfile.ZipFile(self.filename + ".7z", "w", zipfile.ZIP_LZMA) as zipping:
            abs_src = os.path.abspath(self.source)
            for dir_name, sub_dirs, files in os.walk(self.source):
                for file in files:
                    abs_name = os.path.abspath(os.path.join(dir_name, file))
                    arc_name = abs_name[len(abs_src) + 1:]
                    zipping.write(abs_name, arc_name)

    def __str__(self):
        """
        Returns the description of the LZMA-compressed zipfile

        :return: The description of the .7z-file
        """
        return ">>Zipfile with LZMA-compression\n>>Creates a .7z-file with the taken components"


class ZipWithBZIP2Compression(ArchiveEngine):

    def write(self):
        """
        Writes a BZIP2-compressed .bz2-file
        A lot of help from: http://stackoverflow.com/questions/14568647/create-zip-in-python

        :return: none
        """
        with zipfile.ZipFile(self.filename + ".bz2", "w", zipfile.ZIP_BZIP2) as zipping:
            abs_src = os.path.abspath(self.source)
            for dir_name, sub_dirs, files in os.walk(self.source):
                for file in files:
                    abs_name = os.path.abspath(os.path.join(dir_name, file))
                    arc_name = abs_name[len(abs_src) + 1:]
                    zipping.write(abs_name, arc_name)

    def __str__(self):
        """
        Returns the description of the BZIP2-compressed zipfile

        :return: The description of the .bz2-zipfile
        """
        return ">>Zipfile with BZIP2-compression\n>>Creates a .bz2-file with the taken components"


class ZipWithDeflatedCompression(ArchiveEngine):

    def write(self):
        """
        Writes a ZIP_DEFLATED-compressed .zip-file
        A lot of help from: http://stackoverflow.com/questions/14568647/create-zip-in-python

        :return: none
        """
        with zipfile.ZipFile(self.filename + ".zip", "w", zipfile.ZIP_DEFLATED) as zipping:
            abs_src = os.path.abspath(self.source)
            for dir_name, sub_dirs, files in os.walk(self.source):
                for file in files:
                    abs_name = os.path.abspath(os.path.join(dir_name, file))
                    arc_name = abs_name[len(abs_src) + 1:]
                    zipping.write(abs_name, arc_name)

    def __str__(self):
        """
        Returns the description of the ZIP_DEFLATED-compressed zipfile

        :return: The description of the ZIP_DEFLATED zipfile
        """
        return ">>Zipfile with ZIP_DEFLATED-compression\n>>Creates a .zip-file with the taken components"


class TarWithGZIPCompression(ArchiveEngine):

    def write(self):
        """
        Writes a GZIP-compressed .tar.gz-file
        A lot of help from: http://stackoverflow.com/questions/14568647/create-zip-in-python

        :return: none
        """
        with tarfile.TarFile(self.filename + ".tar.gz", "w:gz") as zipping:
            abs_src = os.path.abspath(self.source)
            for dir_name, sub_dirs, files in os.walk(self.source):
                for file in files:
                    abs_name = os.path.abspath(os.path.join(dir_name, file))
                    arc_name = abs_name[len(abs_src) + 1:]
                    zipping.write(abs_name, arc_name)

    def __str__(self):
        """
        Returns the description of the GZIP-compressed .tar.gz-file

        :return: The description of the GZIP-compressed tarfile
        """
        return ">>Tarfile with GZIP-compression\n>>Creates a .tar.gz-file with the taken components"


class TarWithoutCompression(ArchiveEngine):

    def write(self):
        """
        Writes a uncompressed .tar-file
        A lot of help from: http://stackoverflow.com/questions/14568647/create-zip-in-python

        :return: none
        """
        with tarfile.TarFile(self.filename + ".tar", "w") as zipping:
            abs_src = os.path.abspath(self.source)
            for dir_name, sub_dirs, files in os.walk(self.source):
                for file in files:
                    abs_name = os.path.abspath(os.path.join(dir_name, file))
                    arc_name = abs_name[len(abs_src) + 1:]
                    zipping.write(abs_name, arc_name)

    def __str__(self):
        """
        Returns the description of the uncompressed .tar.gz-file

        :return: The description of the uncompressed tarfile
        """
        return ">>Tarfile without compression\n>>Creates a .tar-file with the taken components"


class TarWithLZMACompression(ArchiveEngine):

    def write(self):
        """
        Writes a LZMA-compressed .tar.xz-file
        A lot of help from: http://stackoverflow.com/questions/14568647/create-zip-in-python

        :return: none
        """
        with tarfile.TarFile(self.filename + ".tar.xz", "w:xz") as zipping:
            abs_src = os.path.abspath(self.source)
            for dir_name, sub_dirs, files in os.walk(self.source):
                for file in files:
                    abs_name = os.path.abspath(os.path.join(dir_name, file))
                    arc_name = abs_name[len(abs_src) + 1:]
                    zipping.write(abs_name, arc_name)

    def __str__(self):
        """
        Returns the description of the uncompressed .tar.gz-file

        :return: The description of the uncompressed tarfile
        """
        return ">>Tarfile with LZMA-compression\n>>Creates a .tar.xz-file with the taken components"


class TarWithBZIP2Compression(ArchiveEngine):

    def write(self):
        """
        Writes a BZIP2-compressed .tar.bz2-file
        A lot of help from: http://stackoverflow.com/questions/14568647/create-zip-in-python

        :return: none
        """
        with tarfile.TarFile(self.filename + ".tar.bz2", "w:bz2") as zipping:
            abs_src = os.path.abspath(self.source)
            for dir_name, sub_dirs, files in os.walk(self.source):
                for file in files:
                    abs_name = os.path.abspath(os.path.join(dir_name, file))
                    arc_name = abs_name[len(abs_src) + 1:]
                    zipping.write(abs_name, arc_name)

    def __str__(self):
        """
        Returns the description of the BZIP2-compressed .tar.bz2-file

        :return: The description of the BZIP2-compressed tarfile
        """
        return ">>Tarfile with BZIP2-compression\n>>Creates a .tar.bz2-file with the taken components"
