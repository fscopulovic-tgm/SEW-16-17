"""
@author Filip Scopulovic
@date 12-12-2016
@use Model for the project A10_Shared_Memory
"""

class Model:
    """
    Model for the project A10_Shared_Memory
    """

    def __init__(self):
        """
        Constructor of the model.Model class
        """
        self.__processes = []

    def get_process(self):
        """
        :return self.__processes: Returns the process list
        """
        return self.__processes

    def add_process(self, process):
        """
        Appends a process to the threads list

        :param process: The process that will be added to the self.__processes list

        :return None:
        """
        self.__processes.append(process)

    def del_last_process(self):
        """
        Deletes the last object in the self.__processes list

        :return None:
        """
        self.__processes.pop(-1)