from abc import abstractmethod, ABCMeta
import os

__author__ = 'uhs374h'


class ArchiveEngine(metaclass=ABCMeta):
    def __init__(self, filename, dest):
        """
        Create a new archive run_programm

        :param filename: name of the archive
        :param dest: destination directory
        """
        # get path separator
        sep = os.path.sep

        self.filename = dest + sep + filename
        self.source = None

    @abstractmethod
    def __str__(self):
        """
        A useful description for the archive

        :return: a string representation for the archive
        """

    def set_filelist(self, source):
        """
        set a list of files

        :param source: source files to archive
        :return: None
        """
        self.source = source

    @abstractmethod
    def write(self):
        """
        Write to a archive file

        :return: None
        """
