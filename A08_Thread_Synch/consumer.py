"""
@author: Filip Scopulovic
@date: 21-11-2016
@use: consumer prints out the numbers from the queue
"""
import threading, queue
from watch_dog import Stopable

class Consumer(threading.Thread, Stopable):
    """
    Takes numbers from the queue and prints them out

    :inheritance threading.Thread:
    :inheritance Stopable:
    """
    def __init__(self, queue):
        """
        Calls the Base constructor from threading.Thread
        Initializes both parameters

        :param queue: takes the queue as a parameter
        :param running: takes a boolean that says if the thread should run
        """
        threading.Thread.__init__(self)
        self.queue = queue
        self.running = True

    def stopping(self):
        """
        Class is taken from the abstract class Stopable and it sets the running method False

        :return None:
        """
        self.running = False

    def run(self):
        """
        Prints out the number that waits in the queue while self.running is True

        :return None:
        """
        while self.running:
            if self.queue.empty():
                print("Queue is empty queue element: %s\n" % (str(self.queue.qsize())), end="")
                #self.queue.task_done()
            else:
                print("Random Number is %s, queue element: %s\n" % (str(self.queue.get()), str(self.queue.qsize())), end="")
                self.queue.task_done()