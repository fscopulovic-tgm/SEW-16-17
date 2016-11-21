"""
@author: Filip Scopulovic
@date: 21-11-2016
@use: producer makes a random number and prints it out before putting it in the queue
"""
import threading, random, queue
from watch_dog import Stopable

class Producer(threading.Thread, Stopable):
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
        Makes a random number, prints it out and puts it in the queue

        :return None:
        """
        while self.running:
            rand_num = random.randint(0, 254)
            if self.queue.full():
                print("Queue is full, queue element: %s\n" % (str(self.queue.qsize())), end="")
            else:
                self.queue.put(rand_num)
                print("Made number %s, queue element: %s\n" % (str(rand_num), str(self.queue.qsize())), end="")
            self.queue.join()