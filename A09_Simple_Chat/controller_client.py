"""
@author: Filip Scopulovic
@date: 30-11-2016
@use: Controller for the client
"""

import sys
from PySide import QtCore, QtGui
import view_client, model, client_thread

class Controller_Client(QtGui.QMainWindow):
    """
    Controller for the server GUI

    :inheritance QtGui.QtWidget:
    """

    def __init__(self, parent=None):
        """
        Constructor for the controller of the server

        :param parent:
        """
        super(Controller_Client, self).__init__(parent)

        self.__server_form = view_client.Ui_client_gui()
        self.__model = model.Model()

        self.__server_form.setupUi(self)
        self.__server_form.con_button.clicked.connect(self.new_client)
        self.__server_form.send_button.clicked.connect(self.send_msg)

        self.__chat_text = self.__server_form.chat_client
        self.__msg_text = self.__server_form.message_client

    def new_client(self):
        """
        Initializes a new client

        :return: None
        """
        print("Neuer Client auf dem Weg Cx")
        self.__model.add_new_client()
        print(self.__model.get_client_number())

    def send_msg(self):
        """
        Sends a message to the chat

        :return: None
        """
        self.__chat_text.setText(self.__model.get_chat())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    c = Controller_Client()
    c.show()
    sys.exit(app.exec_())