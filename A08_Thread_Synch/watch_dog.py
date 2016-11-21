"""
@author: Filip Scopulovic
@date: 21-11-2016
@use: watches when the thread needs to be stopped
"""
import threading, time
from abc import ABCMeta, abstractmethod

class Stopable(metaclass=ABCMeta):
    """
    Abstract class for stopping
    """
    @abstractmethod
    def stopping(self):
        """
        Abstract method is necessary to stop a thread in a more secure way

        :return None:
        """
        pass

class WatchDog(threading.Thread):
    """
    Class for stopping a ``Stoppable`` thread

    :inheritance threading.Thread:
    """
    def __init__(self, stoptime, *threads):
        """
        Initializes the WatchDog-Thread

        :param stoptime: takes a time that says when to stop
        :param *threads: a list with threads
        """
        threading.Thread.__init__(self)
        self.stoptime = stoptime
        self.threads = threads

    def run(self):
        """
        Waits the time that is in self.stoptime and stops the threads

        :return None:
        """
        start = time.time()
        end = start + self.stoptime
        # waits until the end of time is reached
        while time.time() < end:
            # sleep should not be more than a second
            time.sleep(0.9)
        # stops all the threads
        for t in self.threads:
            t.stopping()