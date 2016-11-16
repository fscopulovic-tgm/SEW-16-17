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
        print("Producer in")

    def run(self):
        """
        Endless loop that calls the method self.is_prime_number().
        This mehtod returns a boolean and if it is True then it puts the number in the queue,
        else it just increments the number var.

        :return None:
        """
        number = 3
        while True:
            if self.is_prime_number(number):
                self.queue.put(number)
                number += 1
                self.queue.join()
            else:
                number += 1


    def is_prime_number(self, number):
        """
        Looks if the given parameter number is a prime number and returns a bool.

        :param int number: Takes a number
        :return Bool is_prime: Returns
        """
        for i in range(2, number):
            if not i % number == 0:
                return False
        return True