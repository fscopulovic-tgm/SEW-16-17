# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Filip/Desktop/Daten/Schule/4CHIT/SEW_4CHIT/SEW-16-17/A10_Shared_Memory/A10_Main_Window.ui'
#
# Created: Mon Dec 12 11:01:39 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_paint_widget(object):
    """
    GUI for the main_window
    """
    def setupUi(self, paint_widget):
        """
        Sets up the GUI

        :param paint_widget:

        :return None:
        """
        paint_widget.setObjectName("paint_widget")
        paint_widget.resize(554, 435)
        self.gridLayout = QtGui.QGridLayout(paint_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.new_button = QtGui.QPushButton(paint_widget)
        self.new_button.setObjectName("new_button")
        self.gridLayout.addWidget(self.new_button, 1, 0, 1, 1)
        self.remove_button = QtGui.QPushButton(paint_widget)
        self.remove_button.setObjectName("remove_button")
        self.gridLayout.addWidget(self.remove_button, 1, 1, 1, 1)
        self.graphicsView = QtGui.QGraphicsView(paint_widget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.retranslateUi(paint_widget)
        QtCore.QMetaObject.connectSlotsByName(paint_widget)

    def retranslateUi(self, paint_widget):
        """
        Translates the GUI

        :param paint_widget:

        :return None:
        """
        paint_widget.setWindowTitle(QtGui.QApplication.translate("paint_widget", "My Floating Points", None, QtGui.QApplication.UnicodeUTF8))
        self.new_button.setText(QtGui.QApplication.translate("paint_widget", "New Point", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_button.setText(QtGui.QApplication.translate("paint_widget", "Remove Last Point", None, QtGui.QApplication.UnicodeUTF8))

