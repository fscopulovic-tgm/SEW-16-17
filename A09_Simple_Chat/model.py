"""
@author: Filip Scopulovic
@date: 30-11-2016
@use: Model for the MVC-model
"""

class Model:
    """"
    Model that contains a list of clients and getter and setter
    """

    def __init__(self):
        """
        Initializes the clients
        """
        self.__clients = []

    def get_clients(self):
        """
        :return __clients: returns the list of the clients
        """
        return self.__clients

    def add_client(self, client):
        """
        Appends a new client to __clients

        :param client: The needed client

        :return None:
        """
        self.__clients.append(client)

    def del_client(self, client):
        """
        Removes a client from __clients

        :param client: The needed client

        :return None:
        """
        self.__clients.remove(client)