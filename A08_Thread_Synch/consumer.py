"""
@author: Filip Scopulovic
@date: 21-11-2016
@use: consumer prints out the numbers from the queue
"""
import threading, queue, time
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
            time.sleep(0.01)
            if self.queue.empty():
                print("Queue is empty\t\t\t|\t\tqueue element: %s\n\n" % (str(self.queue.qsize())), end="")
                #self.queue.task_done()
            else:
                #Koennte wie beim Producer ein Einzeiler sein, wollte aber einen schoeneren Output haben und deshalb so "kompliziert"
                got_number = self.queue.get()
                if got_number < 10:
                    print("Random number %s\t\t\t|\t\tqueue element: %s\n\n" % (str(got_number), str(self.queue.qsize())), end="")
                else:
                    print("Random number %s\t\t|\t\tqueue element: %s\n\n" % (str(got_number), str(self.queue.qsize())), end="")
                self.queue.task_done()