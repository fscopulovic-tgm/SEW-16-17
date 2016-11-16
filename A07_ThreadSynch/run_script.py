"""
@author: Filip Scopulovic
@date: 11-11-2016
@use: run_script that initializes producer and consumer and starts them
"""
import queue, consumer, producer, os
"""
Starts the threads and if the user gives in a input it reacts to that.
If the user types in exit, it breaks the endless loop and calls the method .join(), so it terminates all the threads

:return None:
"""
queue = queue.Queue()

file = open("files/prime_numbers.txt", 'w')

t_producer = producer.Producer(queue)
t_consumer = consumer.Consumer(queue, file)

t_producer.start()
t_consumer.start()

t_producer.join()
t_consumer.join()
