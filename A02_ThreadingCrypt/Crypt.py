"""
@author fscopulovic-tgm
@date   19.10.2016
@use    A programm that is used for encrypting files
"""

import threading, re, random

_input_message = None
_input_thread = None
_input_mode = None
_input_message_section = None
threads = None
_length_section_message = None

def random_chars_for_dict():
    """
    This function makes a random dict that sets the varibale __dictEncrypted
    that is used to encrypted the message

    :return dict dict_help: A dict with random char as keys and values
    """

    dict_help = {}
    for i in range(90 - 33 + 1):
        random_char = chr(random.randint(33, 90))
        while (random_char in dict_help.values()):
            random_char = chr(random.randint(33, 90))
        dict_help[chr(i + 33)] = random_char

    return dict_help

def input_menu():
    """
    Function that handles the console menu

    :return: None
    """
    global _input_mode
    _input_mode = input("What do you want to do?\n1.Encrypt\n2.Decrypt\n3.New word\n4.New thread number\n5.Exit\n>>")

def type_input_message():
    """
    Function that handles the message input

    :return: None
    """
    global _input_message
    CryptThread.set_encrypted_message("")
    CryptThread.set_decrypted_message("")
    _input_message = input("Type in a message\n>>")
    if int(_input_thread)> len(_input_message)/2 :
        print("Your new message is longer than the threads existing")
        help_str = input("Do you want to type in a new word or a new thread number?\n1.New word\n2.New thread number\n>>")
        if help_str.lower() == "new word" or help_str == "1":
            type_input_message()
        elif help_str.lower() == "new thread number" or help_str == "2":
            type_input_thread_number()

def type_input_thread_number():
    """
    Function that handles the thread number input

    :return: None
    """
    global _input_message_section, _input_thread, _length_section_message, _input_message
    _input_thread = input("Type your numbers of threads\n>>")
    try:
        if int(_input_thread) < 0:
            print("There can't be negative threads\n")
            type_input_thread_number()
        elif int(_input_thread) > len(_input_message)/2:
            print("The thread number is higher than the length of the input message divided by 2!")
            type_input_thread_number()
        else:
            _length_section_message = len(_input_message) / int(_input_thread)
            _input_message_section = re.findall("." * int(_length_section_message) + "?", _input_message)
    except ValueError:
        print("Error, not ints")
        type_input_thread_number()

def make_threads():
    """
    Function for initializing the threads and starting it
    The function also wait at the end until every thread is done

    :return: None
    """
    global _input_message_section, threads
    threads = []
    for i in range(int(_input_thread)):
        if i == int(_input_thread) - 1:
            help_lst = [len(_input_message_section) - 2 , len(_input_message_section) - 1 ]
            thread = CryptThread(_input_message_section, help_lst,_input_mode)
            threads.append(thread)
            threads[i].start()
        else:
            thread = CryptThread(_input_message_section, i, _input_mode)
            threads.append(thread)
            threads[i].start()

    for i in threads:
        i.join()

    if _input_mode.lower() == "encrypt" or _input_mode == "1":
        print(CryptThread.get_encrypted_message())
    elif _input_mode.lower() == "decrypt" or _input_mode == "2":
        if CryptThread.get_decrypted_message() == "":
            print()
        else:
            print(CryptThread.get_decrypted_message())
    input_menu()


_dict_encrypted = random_chars_for_dict()
_dict_encrypted[' '] = ' '

class CryptThread(threading.Thread):
    """
    This class is a thread that
    will encrypt your message
    One thread will make one char of the word
    """

    __encrypted_message = ""
    __decrypted_message = ""
    def __init__(self, user_input, thread_number, crypt_mode):
        """
        Constructor

        :param list user_input: A list with the section of the input
        :param thread_number: Defines which part of the list the thread should encrypt, it should be a integer or a list that contains integers
        :param String crypt_mode: Defines the mode this thread is using
        """
        super(CryptThread, self).__init__()
        self.crypt_mode = crypt_mode
        if type(thread_number) == type([]):
            if len(user_input[thread_number[1]]) == _length_section_message:
                self.user_input = user_input[thread_number[1]]
            else:
                self.user_input = user_input[thread_number[0]] + user_input[thread_number[1]]
        else:
            self.user_input = user_input[thread_number]

    def encrypt(self):
        """
        Function for encrypting

        :return: None
        """
        for i in self.user_input:
            for k in _dict_encrypted:
                if i.upper() == k:
                    CryptThread.__encrypted_message += _dict_encrypted[k]


    def decrypt(self):
        """
        Function for decrypting

        :return: None
        """
        if self.__encrypted_message == "":
            CryptThread.__decrypted_message = _input_message
        else:
            for i in self.__encrypted_message:
                for k, v in _dict_encrypted.items():
                    if i.upper() == v:
                        CryptThread.__decrypted_message += k

    @classmethod
    def get_encrypted_message(cls):
        """
        :return String __encrypted_message: Returns the encrypted message
        """
        return cls.__encrypted_message

    @classmethod
    def get_decrypted_message(cls):
        """
        :return String __decrypted_message: Returns the decrypted message
        """
        return cls.__decrypted_message

    @classmethod
    def set_encrypted_message(cls, encrypted_message):
        """
        You can set a the param value as the __encrypted_message value

        :param encrypted_message:
        :return: None
        """
        cls.__encrypted_message = encrypted_message

    @classmethod
    def set_decrypted_message(cls, decrypted_message):
        """
        You can set a the param value as the __decrypted_message value

        :param decrypted_message:
        :return: None
        """
        cls.__decrypted_message = decrypted_message

    def run(self):
        if self.crypt_mode.lower() == "1" or self.crypt_mode.lower() == "encrypt":
            self.encrypt()
        elif self.crypt_mode.lower() == "2" or self.crypt_mode.lower() == "decrypt":
            self.decrypt()

def starting_crypt():
    """
    Starts a little script that handles the input and
    that is always running unless you type in 'Exit' or '4'

    :return: None
    """
    global _input_message
    print("Welcome to CryptThread!\n")

    _input_message = input("Type in a message\n>>")
    type_input_thread_number()
    while True:
        input_menu()
        if _input_mode.lower() == "encrypt" or _input_mode == "1":
            make_threads()
        elif _input_mode.lower() == "decrypt" or _input_mode == "2":
            make_threads()
        elif _input_mode.lower() == "new word" or _input_mode == "3":
            type_input_message()
        elif _input_mode.lower() == "new thread number" or _input_mode == "4":
            type_input_thread_number()
        elif _input_mode.lower() == "exit" or _input_mode == "5":
            break
        else:
            print("Wrong mode input!\nPlease type in your mode again\n")

# The functions starts a little script
starting_crypt()