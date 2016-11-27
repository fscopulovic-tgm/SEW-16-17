"""
@author: Filip Scopulovic
@date: 21-11-2016
@use: starting script for the project A08_Thread_Synch
"""
import watch_dog, consumer, producer, queue

#Empty list of threads
threads = []
#Initalizes the queue
qu = queue.Queue()
#Sets the maximum size for the queue at 20
qu.maxsize = 20
#Initalizes the Producer
p1 = producer.Producer(qu)
p2 = producer.Producer(qu)
#Initalizes the Consumers
c1 = consumer.Consumer(qu)
c2 = consumer.Consumer(qu)
#Adds all the threads together
threads.append(p1)
threads.append(p2)
threads.append(c1)
threads.append(c2)

running_time = 2
#Initializes the watch dog
w = watch_dog.WatchDog(running_time, *threads)
w.start()
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
w.join()