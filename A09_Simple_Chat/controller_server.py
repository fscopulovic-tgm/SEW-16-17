"""
@author: Filip Scopulovic
@date: 30-11-2016
@use: Controller for the server
"""
import sys
from PySide import QtCore, QtGui
import view_server, model, server_thread

class Controller_Server(QtGui.QMainWindow):
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
        self.model = model.Model()

        self.__server_form.setupUi(self)
        self.__con_clients = self.__server_form.server_show_client
        self.__chat_server = self.__server_form.chat_server

        self.con_server()

    def get_con_clients_text(self):
        """
        :return __con_clients: Returns the text field with the connected clients
        """
        return self.__con_clients.getText()

    def get_chat_server_text(self):
        """
        :return __chat_server: Returns the text field with the chat
        """
        return self.__chat_server.getText()

    def set_chat_server(self, text):
        """
        Sets the text in the text field __chat_serbver

        :param text: Takes a text to set in the __chat_server

        :return None:
        """
        self.__chat_server.setText(self.__chat_server.getText() +"\ntext")

    def set_con_clients(self, client_number):
        """
        Sets the text in the text field __con_clients

        :param text: Takes a text to set in the __con_clients

        :return None:
        """
        self.__con_clients.setText(self.__con_clients.getText() + "\nClient " + client_number + " ist verbunden!")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    c = Controller_Server()
    c.show()
    sys.exit(app.exec_())