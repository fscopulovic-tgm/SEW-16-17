"""
@author: Filip Scopulovic
@date: 30-11-2016
@use: Client thread
"""
import threading, socket, model

class Client_Thread(threading.Thread):

    def __init__(self, host, port):
        """
        Construktor for the client_thread

        :param host: The host address

        :param port: The port number
        """
        threading.Thread.__init__(self)

    def run(self):
        """
        Method for pressing the connecing button

        :return: None
        """
        pass

    def msg_send(self):
        """
        Sends a message to the server/ other clients

        :return: None
        """
        pass