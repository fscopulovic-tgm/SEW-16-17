# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Filip\Desktop\Daten\Schule\4CHIT\SEW_4CHIT\SEW-16-17\PySide_a_simple_game\python_game.ui'
#
# Created: Mon Nov  7 13:22:52 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Spiel(object):
    def setupUi(self, Spiel):
        Spiel.setObjectName("Spiel")
        Spiel.resize(1019, 659)
        Spiel.setMinimumSize(QtCore.QSize(1019, 659))
        Spiel.setMaximumSize(QtCore.QSize(1019, 659))
        self.horizontalLayoutWidget = QtGui.QWidget(Spiel)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(220, 580, 791, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.neustarten = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.neustarten.setFont(font)
        self.neustarten.setObjectName("neustarten")
        self.horizontalLayout.addWidget(self.neustarten)
        self.verlassen = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.verlassen.setFont(font)
        self.verlassen.setObjectName("verlassen")
        self.horizontalLayout.addWidget(self.verlassen)
        self.gridLayoutWidget = QtGui.QWidget(Spiel)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 201, 631))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.falsch = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.falsch.setFont(font)
        self.falsch.setObjectName("falsch")
        self.gridLayout.addWidget(self.falsch, 2, 0, 1, 1)
        self.gesamt = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gesamt.setFont(font)
        self.gesamt.setObjectName("gesamt")
        self.gridLayout.addWidget(self.gesamt, 3, 0, 1, 1)
        self.korrekt = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.korrekt.setFont(font)
        self.korrekt.setObjectName("korrekt")
        self.gridLayout.addWidget(self.korrekt, 1, 0, 1, 1)
        self.offen_zaehler = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.offen_zaehler.setFont(font)
        self.offen_zaehler.setObjectName("offen_zaehler")
        self.gridLayout.addWidget(self.offen_zaehler, 0, 1, 1, 1)
        self.offen = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.offen.setFont(font)
        self.offen.setObjectName("offen")
        self.gridLayout.addWidget(self.offen, 0, 0, 1, 1)
        self.gesamt_zaehler = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gesamt_zaehler.setFont(font)
        self.gesamt_zaehler.setObjectName("gesamt_zaehler")
        self.gridLayout.addWidget(self.gesamt_zaehler, 3, 1, 1, 1)
        self.falsch_zaehler = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.falsch_zaehler.setFont(font)
        self.falsch_zaehler.setObjectName("falsch_zaehler")
        self.gridLayout.addWidget(self.falsch_zaehler, 2, 1, 1, 1)
        self.korrekt_zaehler = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.korrekt_zaehler.setFont(font)
        self.korrekt_zaehler.setObjectName("korrekt_zaehler")
        self.gridLayout.addWidget(self.korrekt_zaehler, 1, 1, 1, 1)
        self.spiel = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spiel.setFont(font)
        self.spiel.setObjectName("spiel")
        self.gridLayout.addWidget(self.spiel, 4, 0, 1, 1)
        self.spiel_zaehler = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spiel_zaehler.setFont(font)
        self.spiel_zaehler.setObjectName("spiel_zaehler")
        self.gridLayout.addWidget(self.spiel_zaehler, 4, 1, 1, 1)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Spiel)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(220, 10, 791, 131))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.gridLayoutWidget_2 = QtGui.QWidget(Spiel)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(219, 149, 791, 421))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.zahl_11 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.zahl_11.setObjectName("zahl_11")
        self.gridLayout_2.addWidget(self.zahl_11, 1, 3, 1, 1)
        self.zahl_1 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.zahl_1.setObjectName("zahl_1")
        self.gridLayout_2.addWidget(self.zahl_1, 0, 0, 1, 1)
        self.zahl_8 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.zahl_8.setObjectName("zahl_8")
        self.gridLayout_2.addWidget(self.zahl_8, 1, 2, 1, 1)
        self.zahl_7 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.zahl_7.setObjectName("zahl_7")
        self.gridLayout_2.addWidget(self.zahl_7, 0, 2, 1, 1)
        self.zahl_2 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.zahl_2.setObjectName("zahl_2")
        self.gridLayout_2.addWidget(self.zahl_2, 1, 0, 1, 1)
        self.zahl_5 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.zahl_5.setObjectName("zahl_5")
        self.gridLayout_2.addWidget(self.zahl_5, 1, 1, 1, 1)
        self.zahl_6 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.zahl_6.setObjectName("zahl_6")
        self.gridLayout_2.addWidget(self.zahl_6, 2, 1, 1, 1)
        self.zahl_3 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.zahl_3.setObjectName("zahl_3")
        self.gridLayout_2.addWidget(self.zahl_3, 2, 0, 1, 1)
        self.zahl_4 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.zahl_4.setObjectName("zahl_4")
        self.gridLayout_2.addWidget(self.zahl_4, 0, 1, 1, 1)
        self.zahl_10 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.zahl_10.setObjectName("zahl_10")
        self.gridLayout_2.addWidget(self.zahl_10, 0, 3, 1, 1)
        self.zahl_9 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.zahl_9.setObjectName("zahl_9")
        self.gridLayout_2.addWidget(self.zahl_9, 2, 2, 1, 1)
        self.zahl_12 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.zahl_12.setObjectName("zahl_12")
        self.gridLayout_2.addWidget(self.zahl_12, 2, 3, 1, 1)
        self.zahl_13 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.zahl_13.setObjectName("zahl_13")
        self.gridLayout_2.addWidget(self.zahl_13, 0, 4, 1, 1)
        self.zahl_14 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.zahl_14.setObjectName("zahl_14")
        self.gridLayout_2.addWidget(self.zahl_14, 1, 4, 1, 1)
        self.zahl_15 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.zahl_15.setObjectName("zahl_15")
        self.gridLayout_2.addWidget(self.zahl_15, 2, 4, 1, 1)

        self.retranslateUi(Spiel)
        QtCore.QObject.connect(self.verlassen, QtCore.SIGNAL("clicked()"), Spiel.close)
        QtCore.QMetaObject.connectSlotsByName(Spiel)

    def retranslateUi(self, Spiel):
        Spiel.setWindowTitle(QtGui.QApplication.translate("Spiel", "Ein simples Spiel", None, QtGui.QApplication.UnicodeUTF8))
        self.neustarten.setText(QtGui.QApplication.translate("Spiel", "Neustarten", None, QtGui.QApplication.UnicodeUTF8))
        self.verlassen.setText(QtGui.QApplication.translate("Spiel", "Verlassen", None, QtGui.QApplication.UnicodeUTF8))
        self.falsch.setText(QtGui.QApplication.translate("Spiel", "Falsch", None, QtGui.QApplication.UnicodeUTF8))
        self.gesamt.setText(QtGui.QApplication.translate("Spiel", "Gesamt", None, QtGui.QApplication.UnicodeUTF8))
        self.korrekt.setText(QtGui.QApplication.translate("Spiel", "Korrekt", None, QtGui.QApplication.UnicodeUTF8))
        self.offen_zaehler.setText(QtGui.QApplication.translate("Spiel", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.offen.setText(QtGui.QApplication.translate("Spiel", "Offen", None, QtGui.QApplication.UnicodeUTF8))
        self.gesamt_zaehler.setText(QtGui.QApplication.translate("Spiel", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.falsch_zaehler.setText(QtGui.QApplication.translate("Spiel", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.korrekt_zaehler.setText(QtGui.QApplication.translate("Spiel", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.spiel.setText(QtGui.QApplication.translate("Spiel", "Spiel", None, QtGui.QApplication.UnicodeUTF8))
        self.spiel_zaehler.setText(QtGui.QApplication.translate("Spiel", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Spiel", "Druecken Sie die Buttons in aufsteigender Reihenfolge!", None, QtGui.QApplication.UnicodeUTF8))
        self.zahl_11.setText(QtGui.QApplication.translate("Spiel", "zahl_11", None, QtGui.QApplication.UnicodeUTF8))
        self.zahl_1.setText(QtGui.QApplication.translate("Spiel", "zahl_1", None, QtGui.QApplication.UnicodeUTF8))
        self.zahl_8.setText(QtGui.QApplication.translate("Spiel", "zahl_8", None, QtGui.QApplication.UnicodeUTF8))
        self.zahl_7.setText(QtGui.QApplication.translate("Spiel", "zahl_7", None, QtGui.QApplication.UnicodeUTF8))
        self.zahl_2.setText(QtGui.QApplication.translate("Spiel", "zahl_2", None, QtGui.QApplication.UnicodeUTF8))
        self.zahl_5.setText(QtGui.QApplication.translate("Spiel", "zahl_5", None, QtGui.QApplication.UnicodeUTF8))
        self.zahl_6.setText(QtGui.QApplication.translate("Spiel", "zahl_6", None, QtGui.QApplication.UnicodeUTF8))
        self.zahl_3.setText(QtGui.QApplication.translate("Spiel", "zahl_3", None, QtGui.QApplication.UnicodeUTF8))
        self.zahl_4.setText(QtGui.QApplication.translate("Spiel", "zahl_4", None, QtGui.QApplication.UnicodeUTF8))
        self.zahl_10.setText(QtGui.QApplication.translate("Spiel", "zahl_10", None, QtGui.QApplication.UnicodeUTF8))
        self.zahl_9.setText(QtGui.QApplication.translate("Spiel", "zahl_9", None, QtGui.QApplication.UnicodeUTF8))
        self.zahl_12.setText(QtGui.QApplication.translate("Spiel", "zahl_12", None, QtGui.QApplication.UnicodeUTF8))
        self.zahl_13.setText(QtGui.QApplication.translate("Spiel", "zahl_13", None, QtGui.QApplication.UnicodeUTF8))
        self.zahl_14.setText(QtGui.QApplication.translate("Spiel", "zahl_14", None, QtGui.QApplication.UnicodeUTF8))
        self.zahl_15.setText(QtGui.QApplication.translate("Spiel", "zahl_15", None, QtGui.QApplication.UnicodeUTF8))
