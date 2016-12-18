# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Filip/Desktop/Daten/Schule/4CHIT/SEW_4CHIT/SEW-16-17/A10_Shared_Memory/A10_Main_Window.ui'
#
# Created: Sun Dec 18 20:52:10 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_paint_widget(object):
    def setupUi(self, paint_widget):
        paint_widget.setObjectName("paint_widget")
        paint_widget.resize(913, 609)
        self.gridLayout = QtGui.QGridLayout(paint_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtGui.QLabel(paint_widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.red_label = QtGui.QLabel(paint_widget)
        self.red_label.setObjectName("red_label")
        self.gridLayout.addWidget(self.red_label, 6, 2, 1, 1)
        self.widget = QtGui.QWidget(paint_widget)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 3)
        self.label = QtGui.QLabel(paint_widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.horizontalSlider_2 = QtGui.QSlider(paint_widget)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout.addWidget(self.horizontalSlider_2, 4, 1, 1, 1)
        self.horizontalSlider_3 = QtGui.QSlider(paint_widget)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.gridLayout.addWidget(self.horizontalSlider_3, 5, 1, 1, 1)
        self.horizontalSlider_4 = QtGui.QSlider(paint_widget)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.gridLayout.addWidget(self.horizontalSlider_4, 6, 1, 1, 1)
        self.new_button = QtGui.QPushButton(paint_widget)
        self.new_button.setObjectName("new_button")
        self.gridLayout.addWidget(self.new_button, 1, 0, 1, 2)
        self.label_3 = QtGui.QLabel(paint_widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.size_label = QtGui.QLabel(paint_widget)
        self.size_label.setObjectName("size_label")
        self.gridLayout.addWidget(self.size_label, 2, 2, 1, 1)
        self.remove_button = QtGui.QPushButton(paint_widget)
        self.remove_button.setObjectName("remove_button")
        self.gridLayout.addWidget(self.remove_button, 1, 2, 1, 1)
        self.green_label = QtGui.QLabel(paint_widget)
        self.green_label.setObjectName("green_label")
        self.gridLayout.addWidget(self.green_label, 4, 2, 1, 1)
        self.horizontalSlider = QtGui.QSlider(paint_widget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 2, 1, 1, 1)
        self.blue_label = QtGui.QLabel(paint_widget)
        self.blue_label.setObjectName("blue_label")
        self.gridLayout.addWidget(self.blue_label, 5, 2, 1, 1)
        self.label_2 = QtGui.QLabel(paint_widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.retranslateUi(paint_widget)
        QtCore.QMetaObject.connectSlotsByName(paint_widget)

    def retranslateUi(self, paint_widget):
        paint_widget.setWindowTitle(QtGui.QApplication.translate("paint_widget", "My Floating Points", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("paint_widget", "Red", None, QtGui.QApplication.UnicodeUTF8))
        self.red_label.setText(QtGui.QApplication.translate("paint_widget", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("paint_widget", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.new_button.setText(QtGui.QApplication.translate("paint_widget", "New Point", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("paint_widget", "Blue", None, QtGui.QApplication.UnicodeUTF8))
        self.size_label.setText(QtGui.QApplication.translate("paint_widget", "1 px", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_button.setText(QtGui.QApplication.translate("paint_widget", "Remove Last Point", None, QtGui.QApplication.UnicodeUTF8))
        self.green_label.setText(QtGui.QApplication.translate("paint_widget", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.blue_label.setText(QtGui.QApplication.translate("paint_widget", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("paint_widget", "Green", None, QtGui.QApplication.UnicodeUTF8))

