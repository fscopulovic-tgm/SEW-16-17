# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Filip\Desktop\Daten\Schule\4CHIT\SEW_4CHIT\SEW-16-17\A09_Simple_Chat\gui_client.ui'
#
# Created: Thu Dec  1 08:24:40 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_client_gui(object):
    """
    Class for the client GUI
    """
    def setupUi(self, client_gui):
        """
        Sets the client GUI

        :param client_gui:

        :return None:
        """
        client_gui.setObjectName("client_gui")
        client_gui.resize(384, 256)
        self.centralwidget = QtGui.QWidget(client_gui)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.con_button = QtGui.QPushButton(self.centralwidget)
        self.con_button.setObjectName("con_button")
        self.gridLayout.addWidget(self.con_button, 0, 0, 1, 1)
        self.con_label = QtGui.QLabel(self.centralwidget)
        self.con_label.setObjectName("con_label")
        self.gridLayout.addWidget(self.con_label, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.message_client = QtGui.QLineEdit(self.centralwidget)
        self.message_client.setObjectName("message_client")
        self.gridLayout.addWidget(self.message_client, 1, 1, 1, 1)
        self.send_button = QtGui.QPushButton(self.centralwidget)
        self.send_button.setObjectName("send_button")
        self.gridLayout.addWidget(self.send_button, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.chat_client = QtGui.QTextBrowser(self.centralwidget)
        self.chat_client.setObjectName("chat_client")
        self.gridLayout.addWidget(self.chat_client, 4, 0, 1, 2)
        client_gui.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(client_gui)
        self.statusbar.setObjectName("statusbar")
        client_gui.setStatusBar(self.statusbar)

        self.retranslateUi(client_gui)
        QtCore.QMetaObject.connectSlotsByName(client_gui)

    def retranslateUi(self, client_gui):
        """
        Retranslates the UI

        :param client_gui:

        :return None:
        """
        client_gui.setWindowTitle(QtGui.QApplication.translate("client_gui", "Client ", None, QtGui.QApplication.UnicodeUTF8))
        self.con_button.setText(QtGui.QApplication.translate("client_gui", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.con_label.setText(QtGui.QApplication.translate("client_gui", "Status: Not connected", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("client_gui", "Message:", None, QtGui.QApplication.UnicodeUTF8))
        self.send_button.setText(QtGui.QApplication.translate("client_gui", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("client_gui", "Chat:", None, QtGui.QApplication.UnicodeUTF8))

