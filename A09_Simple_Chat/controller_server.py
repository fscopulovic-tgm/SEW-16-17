"""
@author: Filip Scopulovic
@date: 30-11-2016
@use: Controller for the server
"""
import sys
from PySide import QtCore, QtGui
import view_server, model

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
        self.__server_form.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    c = Controller_Server()
    c.show()
    sys.exit(app.exec_())