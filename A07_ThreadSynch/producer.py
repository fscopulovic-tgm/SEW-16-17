"""
@author: Filip Scopulovic
@date: 16-11-2016
@use: Producer searches for prime numbers and gives them to the consumer
"""
import threading, queue

class Producer(threading.Thread):
    """
    class Producer that inheritance from threading.Thread
    Takes prime numbers and gives it to the Consumer class

    :inheritance threading.Thread:
    """

    def __init__(self, queue):
        """
        Constructor of the Producer class

        :param queue: takes the queue as a parameter
        """
        threading.Thread.__init__(self)
        self.queue = queue

        def run(self):
            """


            :return None:
            """
            pass