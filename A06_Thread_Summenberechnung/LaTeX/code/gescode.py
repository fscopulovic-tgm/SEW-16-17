"""
@author: Filip Scopulovic
@date: 11-11-2016
@use: Threading Klasse; Benutzer gibt eine Zahl ein und diese werden dann aufaddiert
"""
import threading, time

class Summenberechnung(threading.Thread):
    """
    User gives a input and then it sums the numbers from 1 to the input number
    It works with three threads
    class-attributes: counter, lock
    :inheritance threading.Thread:
    """
    #counter is here for counting up and knowing what number a thread is using
    __counter = 0

    #lock is here to lock the attribute counter so the threads won't interrupt themself
    __lock = threading.Lock()


    def __init__(self, sum_list):
        """
        Constructor that calls the super-constructor from the threading.Thread class
        """
        threading.Thread.__init__(self)
        self.start_time = time.time()
        self.sum_list = sum_list

    def run(self):
        """
        run-method from the constructor
        Here is everything that the threads will do
        :return None:
        """
        for i in range(len(self.sum_list)):
            with Summenberechnung.__lock:
                Summenberechnung.__counter += self.sum_list[i]
                #print("Current number: %s" % (Summenberechnung.__counter))
        end_time = time.time()
        print(end_time - self.start_time)

    def get_counter(self):
        """
        Returns the counter
        :return Summenberechnung.__counter:
        """
        return Summenberechnung.__counter

def make_input_list():
    """
    Method that takes care of the input
    Checks what inputs are in and if one is not okay it runs the method another time
    Initialise a list that has every number of the input number in it
    :return None:
    """
    input_list = []
    input_number = input("Write a number that you want to sum!\n>>")
    try:
        for i in range(int(input_number)):
            input_list += [i]
        if int(input_number) < 0:
            print("No negative numbers")
            make_input_list()
        else:
            input_div_three(input_list, input_number)
    except ValueError:
        print("The input is not a number!")
        make_input_list()

def partition(lst):
    """
    Method idea from http://stackoverflow.com/questions/2659900/python-slicing-a-list-into-n-nearly-equal-length-partitions
    :param lst:
    :return [lst[int(round(division * i)): int(round(division * (i + 1)))] for i in range(3)]: return a list, that has lists in it, those lists are seperated in the number what division got
    """
    div_three = len(lst) / 3
    return [lst[int(round(div_three * i)): int(round(div_three * (i + 1)))] for i in range(3)]

def input_div_three(input_number_list, last_number):
    """
    Takes the input number list and cuts this through three
    :param input_number:
    :param last_number:
    :return None:
    """
    div_three_list = partition(input_number_list)
    #Need to add the input number, because the partition method does not put the input number in the list
    div_three_list[2] += [int(last_number)]
    print(div_three_list)
    start_threads(div_three_list)

def start_threads(div_sum_list):
    """
    Starts the threads and gives them their list
    :param div_sum_list:
    :return None:
    """
    threads = []
    #Initialize 3 threads of the class Summenberechung and starts them
    for i in range(3):
        thread = Summenberechnung(div_sum_list[i])
        threads += [thread]
        thread.start()

    #waits for the children-threads
    for x in threads:
        x.join()

    #prints the summed number out
    print("Sum of the numbers: %s" %(str(Summenberechnung.get_counter(Summenberechnung))))

make_input_list()