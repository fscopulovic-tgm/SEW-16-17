# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Filip/Desktop/Daten/Schule/4CHIT/SEW_4CHIT/SEW-16-17/A10_Shared_Memory/A10_PointOption_Window.ui'
#
# Created: Sun Dec 18 19:22:35 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_point_options(object):
    def setupUi(self, point_options):
        point_options.setObjectName("point_options")
        point_options.resize(482, 379)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(point_options.sizePolicy().hasHeightForWidth())
        point_options.setSizePolicy(sizePolicy)
        point_options.setMinimumSize(QtCore.QSize(234, 169))
        point_options.setMaximumSize(QtCore.QSize(1234556, 1215124))
        self.gridLayout = QtGui.QGridLayout(point_options)
        self.gridLayout.setObjectName("gridLayout")
        self.color_watch = QtGui.QGraphicsView(point_options)
        self.color_watch.setMaximumSize(QtCore.QSize(75, 50))
        self.color_watch.setObjectName("color_watch")
        self.gridLayout.addWidget(self.color_watch, 4, 2, 1, 1)
        self.label_4 = QtGui.QLabel(point_options)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(point_options)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(point_options)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(point_options)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtGui.QLabel(point_options)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(point_options)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)
        self.green_slider = QtGui.QSlider(point_options)
        self.green_slider.setOrientation(QtCore.Qt.Horizontal)
        self.green_slider.setObjectName("green_slider")
        self.gridLayout.addWidget(self.green_slider, 1, 1, 1, 3)
        self.red_slider = QtGui.QSlider(point_options)
        self.red_slider.setOrientation(QtCore.Qt.Horizontal)
        self.red_slider.setObjectName("red_slider")
        self.gridLayout.addWidget(self.red_slider, 2, 1, 1, 3)
        self.blue_slider = QtGui.QSlider(point_options)
        self.blue_slider.setOrientation(QtCore.Qt.Horizontal)
        self.blue_slider.setObjectName("blue_slider")
        self.gridLayout.addWidget(self.blue_slider, 3, 1, 1, 3)
        self.abort_button = QtGui.QPushButton(point_options)
        self.abort_button.setObjectName("abort_button")
        self.gridLayout.addWidget(self.abort_button, 5, 3, 1, 1)
        self.create_button = QtGui.QPushButton(point_options)
        self.create_button.setObjectName("create_button")
        self.gridLayout.addWidget(self.create_button, 5, 0, 1, 3)
        self.size_slider = QtGui.QSlider(point_options)
        self.size_slider.setOrientation(QtCore.Qt.Horizontal)
        self.size_slider.setObjectName("size_slider")
        self.gridLayout.addWidget(self.size_slider, 0, 2, 1, 1)

        self.retranslateUi(point_options)
        QtCore.QMetaObject.connectSlotsByName(point_options)

    def retranslateUi(self, point_options):
        point_options.setWindowTitle(QtGui.QApplication.translate("point_options", "Point Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("point_options", "Blue", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("point_options", "Green", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("point_options", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("point_options", "Red", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("point_options", "Size:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("point_options", "x px", None, QtGui.QApplication.UnicodeUTF8))
        self.abort_button.setText(QtGui.QApplication.translate("point_options", "Abort", None, QtGui.QApplication.UnicodeUTF8))
        self.create_button.setText(QtGui.QApplication.translate("point_options", "Create", None, QtGui.QApplication.UnicodeUTF8))

