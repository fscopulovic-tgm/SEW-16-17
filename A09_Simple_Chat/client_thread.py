"""
@author: Filip Scopulovic
@date: 30-11-2016
@use: Client thread
"""
import threading, socket, model, controller_client

class Client_Thread(threading.Thread):

    # TODO add a model as a parameter
    def __init__(self, host, port):
        """
        Construktor for the client_thread

        :param host: The host address

        :param port: The port number
        """
        threading.Thread.__init__(self)
        self.__client_gui = controller_client.Controller_Client()

    def run(self):
        """
        Method for pressing the connecing button

        :return: None
        """


    def msg_send(self):
        """
        Sends a message to the server/ other clients

        :return: None
        """
        pass

class Listening_Server_Thread(threading.Thread):
    """
    Listens if something happens and reacts to it
    """

    def __init__(self):

        threading.Thread.__init__(self)

    def run(self):
        pass