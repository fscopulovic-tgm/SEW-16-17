"""
@author: Filip Scopulovic
@date: 30-11-2016
@use: Controller and Listening_Thread for the client
"""
# Martin Woelfer showed and helped me a lot with the Listening_Thread_Client

import sys
from PySide.QtCore import *
from PySide.QtGui import *
import model, socket, view_client

class Listening_Thread_CLient(QThread):
    """
    Class that contains a Thread that listens if something happens

    :inheritance QThread: QThread is a thread from the module QtCore
    """

    def __init__(self, clientsocket):
        """
        Constructor for the Listening_Thread

        :param clientsocket: Takes the clientsocket as a parameter
        """
        QThread.__init__(self)
        self.__clientsocket = clientsocket

    def run(self):
        """
        The thread wait until some data is received, if it is received then
        the thread will send a signal to the method 'update_chat(text)'

        :return: None
        """
        try:
            while True:
                recv_msg = self.__clientsocket.recv(1024).decode()
                if not recv_msg:
                    self.__clientsocket.close()
                    break
                self.emit(SIGNAL('update_chat(QString)'), recv_msg)
        except socket.error as serr:
            print("Socket error: " + serr.strerror)

class Controller_Client(QMainWindow):
    """
    Controller for the server GUI

    :inheritance QMainWindow:
    """

    def __init__(self, parent=None):
        """
        Constructor for the controller of the server

        :param parent:
        """
        super(Controller_Client, self).__init__(parent)

        self.__client_form = view_client.Ui_client_gui()
        self.__model = model.Model()

        self.__client_form.setupUi(self)
        self.__client_form.con_button.clicked.connect(self.__connect_client)

        self.__chat_text = self.__client_form.chat_client
        self.__msg_text = self.__client_form.message_client
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__listening_thread = Listening_Thread_CLient(self.__client_socket)

    def __connect_client(self):
        """
        Connects a client with the server
        Is used when the connect-button is pressed

        :return: None
        """
        con = False
        try:
            self.__client_socket.connect(('localhost', 12345))
            self.__client_form.send_button.clicked.connect(self.__send_msg)
            con = True
        except socket.error as serr:
            print("Socket error: " + serr.strerror)

        if con:
            self.__client_form.con_label.setText("Connected!")
            self.__client_form.con_button.setEnabled(False)

            self.connect(self.__listening_thread, SIGNAL("update_chat(QString)"), self.update_chat)

            self.__listening_thread.start()

    def update_chat(self, text):
        """
        Adds the text to the chat

        :param text: text that will be added to the chat

        :return: None
        """
        self.__chat_text.append(text)

    def __send_msg(self):
        """
        Sends a message to the chat and also sets it in the chat

        :return: None
        """
        try:
            self.__client_socket.send(self.__msg_text.text().encode())
            self.__msg_text.clear()
        except socket.error as serr:
            print("Socket error: " + serr.strerror)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Controller_Client()
    c.show()
    sys.exit(app.exec_())