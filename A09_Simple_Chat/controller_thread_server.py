"""
@author: Filip Scopulovic
@date: 30-11-2016
@use: Controller for the server
"""
# Martin Woelfer showed and helped me a lot with the Listening_Thread_Server and the Client_Thread

import sys
from PySide.QtCore import *
from PySide.QtGui import *
import view_server, model, socket

class Listening_Thread_Server(QThread):
    """
    Class that contains a Thread that listens if something happens

    :inheritance QThread: QThread is a thread from the module QtCore
    """

    def __init__(self, chat, model, controller, max_clients=10):
        """
        Constructor for the Listening_Thread_Server

        :param chat: A parameter that takes the chat window

        :param model: A parameter that takes the model

        :param controller: A parameter that takes the controller

        :param max_clients: A parameter that contains the value of the maximum clients, is set with 10
        """
        QThread.__init__(self)
        self.__model = model
        self.__controller = controller

        self.__serversocket = socket.socket()
        self.__serversocket.bind(('localhost', 12345))
        self.__serversocket.listen(max_clients)
        self.__chat = chat
        self.__client_number = 0

    def run(self):
        """
        Accepts a client and after accepting it, it creates a new thread for it.
        This client gets added to the __clients list in the model

        :return None:
        """
        try:
            while True:
                (clientsocket, address) = self.__serversocket.accept()
                self.__client_number += 1
                client_thread = Client_Thread(self.__model, "Client " + self.__client_number, clientsocket, self)
                self.model.add_client(client_thread)

                self.connect(client_thread, SIGNAL("write_clients()"), self.__controller.write_clients)
                self.connect(client_thread, SIGNAL("write_chat_server()"), self.__controller.write_chat_server)

                client_thread.start()
                self.emit(SIGNAL('write_chat_server()'))
        except socket.error as serr:
            print("Socket closed")

    def minus_client_number(self):
        """
        __client_number minus 1

        :return None:
        """
        self.__client_number -= 1

class Client_Thread(QThread):
    """
    A class Client_Thread that controlls the socket commands
    """

    def __init__(self, model, name, clientsocket, listening_thread):
        """
        Initialize variables

        :param model: Model to have access to the clients-list

        :param name: Name of the client, that will be set something like 'Client 1'

        :param clientsocket: Clientsocket

        :param listening_thread: The listening_thread
        """
        QThread.__init__(self)
        self.__model = model
        self.__name = name
        self.__clientsocket = clientsocket
        self.__listening_thread = listening_thread

    def run(self):
        """
        Waits for receiving message from the client

        If the Client was disconnected, this object is removed from the list and the list is updated

        :return: void
        """
        while True:
            recv_msg = self.__clientsocket.recv(1024).decode()
            if not recv_msg:
                self.__clientsocket.close()
                self.__model.del_clients(self)
                self.emit(SIGNAL('write_clients()'))
                self.__listening_thread.minus_client_number()
                break
            self.emit(SIGNAL('write_chat_server(QString, QString)'), self.__name, recv_msg)
            for client in self.__model.get_clients:
                client.send_message(self.__name + ": " + recv_msg)

    def get_name(self):
        """
        :return self.__name: The name of the client
        """
        return self.__name

    def send_msg(self, text):
        """
        Sends a encoded text

        :param text: A parameter for the text that will be send

        :return None:
        """
        self.__clientsocket.send(msg.encode())

class Controller_Server(QMainWindow):
    """
    Controller for the server GUI

    :inheritance QtGui.QtWidget:
    """

    def __init__(self, parent=None):
        """
        Constructor for the controller of the server

        :param parent:
        """
        super(Controller_Server, self).__init__(parent)

        self.__server_form = view_server.Ui_server_gui()
        self.__model = model.Model()

        self.__server_form.setupUi(self)
        self.__server_show_client = self.__server_form.server_show_client
        self.__chat_server = self.__server_form.chat_server
        self.__listening_thread = Listening_Thread_Server(self.__chat_server, self.__model, self)
        self.connect(self.__listening_thread, SIGNAL("write_clients()"), self.write_clients)

    def write_chat_server(self, client, text):
        """
        Writes in the text-field __chat_serbver

        :param client: A parameter for the client that wrote something

        :param text: Takes a text to set in the __chat_server

        :return None:
        """
        self.__chat_server.append(client + ": " + text)

    def write_clients(self):
        """
        Writes in the text-field __server_show_client if there is a
        disconnect or a new connection

        :return None:
        """
        self.__server_show_client.clear()
        for client in self.__model.get_clients:
            self.__server_show_client.append(client.get_name())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Controller_Server()
    c.show()
    sys.exit(app.exec_())