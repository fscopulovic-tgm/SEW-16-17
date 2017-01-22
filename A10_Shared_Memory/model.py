"""
@author Filip Scopulovic
@date 12-12-2016
@use Model for the project A10_Shared_Memory
"""
from multiprocessing import Process
from random import randint
import time

class Model:
    """
    Model for the project A10_Shared_Memory
    """

    def __init__(self, win_size, sleep_time, max_speed):
        """
        Constructor of the model.Model class

        :param win_size: Window size

        :param max_speed: Maximal speed for the points
        """
        self.__processes = []
        self.__win_size = win_size
        self.__max_speed = max_speed
        self.__sleep_time = sleep_time

    def get_process(self):
        """
        :return self.__processes: Returns the process list
        """
        return self.__processes

    def new_point(self, size, color):
        """
        Appends a process to the threads list

        :param size: Size of the point
        :param color: Color of the point

        :return None:
        """
        attributes = {'size': size,
                      'color': color,
                      'win_size': self.__win_size,
                      'max_speed': self.__max_speed,
                      'sleep_time': self.__sleep_time}
        point = Point(attributes)
        point.start()
        self.__processes += [point]

    def del_last_process(self):
        """
        Deletes the last object in the self.__processes list

        :return None:
        """
        self.__processes[-1].shutdown()
        self.__processes[-1].join()
        self.__processes.pop(-1)

    def del_all_process(self):
        """
        Deletes all the processes

        :return None:
        """
        for p in self.__processes:
            p.shutdown()
            p.join()
            self.__processes.pop(0)

class Point(Process):
    """
    Class that contains a point, which is also a Process
    """

    def __init__(self, attributes):
        """
        Constructor of the class

        :param attributes: Contains all attributes of the point
        """
        Process.__init__(self)
        self.size = attributes['size']
        self.color = attributes['color']
        self.__win_size = attributes['win_size']
        self.__max_speed = attributes['max_speed']
        self.__sleep_time = attributes['sleep_time']

        self.__running = True

        self.__x_pos = randint(1, self.__win_size[0])
        self.__y_pos = randint(1, self.__win_size[1])

        self.__x_step = randint(1, self.__max_speed)
        self.__y_step = randint(1, self.__max_speed)

        self.__x_dir = randint(1, 2)
        self.__y_dir = randint(1, 2)

    def run(self):
        """
        Run method for the process

        :return None:
        """
        while self.__running:
            self.__x_pos = self.__x_step * self.__x_dir
            self.__y_pos = self.__y_step * self.__y_dir

    def shutdown(self):
        """
        Sets the running value to False

        :return None:
        """
        self.__running = False
