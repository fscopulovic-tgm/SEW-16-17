"""
@author: Filip Scopulovic
@date: 11-11-2016
@use: Consumer prints the prime number out that the producer finds
"""
import threading

class Consumer(threading.Thread):
    """
    class Consumer that inheritance from threading.Thread
    Prints prime numbers, that it takes from the Producer class

    :inheritance threading.Thread:
    """

    def __init__(self, queue, prime_file):
        """
        Constructor of the Consumer class.

        :param Queue queue: takes the queue as a parameter
        :param object prime_file: a file where the Consumer writes the prime numbers in
        """
        threading.Thread.__init__(self)
        self.queue = queue
        self.prime_file = prime_file

    def run(self):
        """
        Endless loop that waits for the producer to get the prime numbers from the queue.
        Prints out the prime number in the console and write it in a .txt-file.

        :return None:
        """
        while True:
            number = self.queue.get()
            print("Found prime number is %s" % (str(number)))
            self.prime_file.write(str(number) + "\n")
            self.queue.task_done()