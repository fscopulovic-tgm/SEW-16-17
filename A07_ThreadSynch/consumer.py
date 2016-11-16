"""
@author: Filip Scopulovic
@date: 11-11-2016
@use: Consumer prints the prime number out that the producer finds
"""
import threading, queue

class Consumer(threading.Thread):
    """
    class Consumer that inheritance from threading.Thread
    Prints prime numbers, that it takes from the Producer class

    :inheritance threading.Thread:
    """

    def __init__(self, queue):
        """
        Constructor of the Consumer class

        :param queue: takes the queue as a parameter
        """
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        """


        :return None:
        """
        pass