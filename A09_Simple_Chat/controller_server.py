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

    def con_server(self):
        """
        Method for starting a server thread, will start when the GUI starts

        :return: None
        """
        server = server_thread.Server_Thread(self.model.get_host())
        server.bind_server()

        self.model.set_port(server.get_port_number())

        server.start()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    c = Controller_Server()
    c.show()
    sys.exit(app.exec_())