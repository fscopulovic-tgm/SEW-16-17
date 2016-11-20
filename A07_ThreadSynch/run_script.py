"""
@author: Filip Scopulovic
@date: 11-11-2016
@use: run_script that initializes producer and consumer and starts them
"""
import queue, consumer, producer

class Run_script:
    """
    Class I made for starting the Consumer and producer
    I just made the class so my docstrings will be recognized by Sphinx
    """

    def __init__(self):
        """
        Initializes the queue, the file, the Consumer and the Producer and calls the start_threads() method
        """
        self.queue = queue.Queue()

        self.file = open("prime_numbers.txt", 'w')

        self.t_producer = producer.Producer(self.queue)
        self.t_consumer = consumer.Consumer(self.queue, self.file)

        self.start_threads()


    def start_threads(self):
        """
        Calls the methods start() and join() from Producer and Consumer

        :return None:
        """
        self.t_producer.start()
        self.t_consumer.start()

        self.t_producer.join()
        self.t_consumer.join()


rs = Run_script()