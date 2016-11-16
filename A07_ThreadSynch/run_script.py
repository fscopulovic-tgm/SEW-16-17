"""
@author: Filip Scopulovic
@date: 11-11-2016
@use: run_script that initializes producer and consumer and starts them
"""
import queue, consumer, producer

queue = queue.Queue()

t_producer = producer.Producer(queue)
t_consumer = consumer.Consumer(queue)

t_producer.start()
t_consumer.start()

t_producer.join()
t_consumer.join()