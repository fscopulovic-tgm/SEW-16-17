"""
@author: Filip Scopulovic
@date: 30-11-2016
@use: Model for both client and server
"""

class Model:
    """"
    Model that has every variable in it
    """

    def __init__(self):
        """
        Constructor for the model
        Initializes every variable that is needed
        """
        self.__host = 'localhost'
        self.__port = 0
        self.__threads = []
        self.__client_number = 0
        self.__chat = ""

    def get_host(self):
        """
        :return self.__host: Returns the host number
        """
        return self.__host

    def get_port(self):
        """
        :return self.__port: Returns the port number
        """
        return self.__port

    def set_port(self, port_number):
        """
        Sets the port number

        :return: None
        """
        self.__port = port_number

    def get_threads(self):
        """
        :return self.threads: Returns the list of threads
        """
        return self.__threads

    def add_thread(self, thread):
        """
        Adds a thread to the self.__threads list

        :return: None
        """
        self.__threads.append(thread)

    def get_client_number(self):
        """
        :return self.__client_number: Returns the client number
        """
        return self.__client_number

    def add_new_client(self):
        """
        Increments the self.__client_number method

        :return: None
        """
        self.__client_number += 1

    def get_chat(self):
        """
        :return self.__chat: Returns the chat
        """
        return self.__chat

    # TODO Client der gesendet hat, muss hinzugefügt werden
    def update_chat(self, client_number,to_update):
        """
        Updates the chat

        :return: None
        """
        self.__chat += "Client " + client_number + ":" + to_update + "\n"