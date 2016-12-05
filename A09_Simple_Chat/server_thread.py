"""
@author: Filip Scopulovic
@date: 30-11-2016
@use: Server thread
"""
import threading, socket, controller_server, model

class Server_Thread(threading.Thread):
    
    # TODO add a model as a parameter
    def __init__(self, host):
        """
        Construktor for the client_thread

        :param host: The host address

        :param port: The port number
        """
        threading.Thread.__init__(self)
        self.__host = host
        self.__port = 0
        self.__max_clients = 10
        self.__serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_gui = controller_server.Controller_Server()

    def run(self):
        """
        Method for pressing the connecing button

        :return: None
        """
        self.__server_gui.show()

    def bind_server(self):
        """
        Binds the server

        :return: None
        """
        self.__serversocket.bind((self.__host, self.__port))
        self.__serversocket.listen(self.__max_clients)

    def get_port_number(self):
        """
        :return self.__serversocket.getsockname()[1]: Returns the port number that is picked by the OS
        """
        return self.__serversocket.getsockname()[1]

class Listening_Server_Thread(threading.Thread):
    """
    Listens if something happens and reacts to it
    """

    def __init__(self):

        threading.Thread.__init__(self)

    def run(self):
        pass