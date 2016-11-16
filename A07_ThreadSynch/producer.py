"""
@author: Filip Scopulovic
@date: 16-11-2016
@use: Producer searches for prime numbers and gives them to the consumer
"""
import threading, queue, math

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
        number = 0
        while True:
            if self.is_prime_number(number):
                self.queue.put(number)
                self.queue.join()
            number += 1


    def is_prime_number(self, number):
        """
        Looks if the given parameter number is a prime number and returns a Boolean.
        Idea from the method came from the website http://stackoverflow.com/questions/18833759/python-prime-number-checker

        :param int number: Takes a number
        :return bool is_prime: Returns a Boolean to see if the given number is a prime number
        """
        if number % 2 == 0 and number > 2:
            return False
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            if number % i == 0:
                return False
        return True