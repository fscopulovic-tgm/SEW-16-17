# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Filip\Desktop\Daten\Schule\4CHIT\SEW_4CHIT\SEW-16-17\A09_Simple_Chat\gui_server.ui'
#
# Created: Wed Nov 30 15:43:35 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_server_gui(object):
    """
    Class for server GUI
    """

    def setupUi(self, server_gui):
        """
        Sets the server GUI

        :param server_gui:

        :return None:
        """
        server_gui.setObjectName("server_gui")
        server_gui.resize(346, 319)
        self.centralwidget = QtGui.QWidget(server_gui)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.server_show_client = QtGui.QTextBrowser(self.centralwidget)
        self.server_show_client.setObjectName("server_show_client")
        self.gridLayout.addWidget(self.server_show_client, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.chat_server = QtGui.QTextBrowser(self.centralwidget)
        self.chat_server.setObjectName("chat_server")
        self.gridLayout.addWidget(self.chat_server, 3, 0, 1, 1)
        server_gui.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(server_gui)
        self.statusbar.setObjectName("statusbar")
        server_gui.setStatusBar(self.statusbar)

        self.retranslateUi(server_gui)
        QtCore.QMetaObject.connectSlotsByName(server_gui)

    def retranslateUi(self, server_gui):
        """
        Retranslates the UI

        :param server_gui:

        :return None:
        """
        server_gui.setWindowTitle(QtGui.QApplication.translate("server_gui", "Server", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("server_gui", "Connected Clients:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("server_gui", "Chat:", None, QtGui.QApplication.UnicodeUTF8))

