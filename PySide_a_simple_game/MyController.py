"""
@author: Filip Scopulovic
@date: 07-11-2016
@use: Kontroller, der die GUI und das Model vereint
"""
import sys
from PySide import QtCore, QtGui
from MyView import Ui_Spiel
from random import Random
import MyView, MyModel

class MeinKontroller(QtGui.QWidget):
    """
    Kontroller der GUI
    """

    def __init__(self, parent=None):
        """
        Konstruktor des Kontrollers

        :param parent:
        """
        super(MeinKontroller, self).__init__()

        self.__myForm = MyView.Ui_Spiel()
        self.__myForm.setupUi(self)
        self.__model = MyModel.MeinModel()

        #Vorhanden ist eine Liste mit den schon vorhanden Zahlen
        self.__vorhanden = []

        #Dieser Abschnitt ist dafuer da, die Zahlbuttons aus der View zu bekommen
        self.__buttons = []
        for i in range(1, 16):
            #Mit Format werden die Namen der Buttons initialisiert
            gewaehlter_button = "zahl_{0}".format(i)
            #Mit getattr werden die Buttons zurueckgeliefert
            zahl_button = getattr(self.__myForm, gewaehlter_button)
            #Man addet die Buttons in eine Liste
            self.__buttons.append(zahl_button)

        #Dieser Abschnitt kuemmert sich darum, das die Buttons mit ihren Methoden verbinden werden
        self.__myForm.neustarten.clicked.connect(self.__spiel_neustarten)
        #Ich wusste nicht wie man die Buttons mit einer For-Schleife mit einem Signal verbindet,
        #also habe ich den Schüler Pierre Rieger gefragt und er hat mir dann durch seine Hilfe die for-Schleife erklärt
        for b in self.__buttons:
            b.clicked.connect(lambda b=b: self.__zahl_button_geklickt(b))

        self.__labels_updaten()
        self.__set_zahl_button()

    def __spiel_neustarten(self):
        """
        Startet das Spiel neu, indem es die Labels zuruecksetzt mit einer Methode aus dem Model
        und eine Methode, die die Buttons neu setzt

        :return: None
        """
        self.__model.zuruecksetzen()
        self.__model.plus_spiel()
        self.__labels_updaten()
        self.__set_zahl_button()

    def __zahl_button_geklickt(self, btn):
        """
        Gibt an, was passiert, wenn ein Zahl Button geklickt wurde

        :param btn:
        :return: None
        """
        geklickter_button = int(btn.text())
        if geklickter_button == self.__vorhanden[0]:
            btn.setEnabled(False)
            self.__model.minus_offene_buttons()
            self.__model.plus_korrekt()
            self.__vorhanden.pop(0)
        else:
            self.__model.plus_falsch()
        self.__labels_updaten()

    def __labels_updaten(self):
        """
        Aktualisiert die Labels mit neuen Werten

        :return: None
        """
        self.__myForm.offen_zaehler.setText(str(self.__model.get_offene_buttons()))
        self.__myForm.korrekt_zaehler.setText(str(self.__model.get_korrekt()))
        self.__myForm.falsch_zaehler.setText(str(self.__model.get_falsch()))
        self.__myForm.gesamt_zaehler.setText(str(self.__model.get_gesamt()))
        self.__myForm.spiel_zaehler.setText(str(self.__model.get_spiele()))

    def __set_zahl_button(self):
        """
        Setzt den Text für die Buttons

        :return: None
        """
        zufall = Random()
        nichtvorhanden = list(range(1, len(self.__buttons) + 1))

        #Einige dieser Stellen wurden ebenfalls mit der Hilfestellung von Pierre Rieger fertiggestellt
        for b in self.__buttons:
            b.setEnabled(True)
            zufall_index = zufall.randint(0, len(nichtvorhanden) - 1)
            zufalls_nummer = nichtvorhanden.pop(zufall_index)
            b.setText(str(zufalls_nummer))
            self.__vorhanden.append(zufalls_nummer)

        self.__vorhanden.sort()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    c = MeinKontroller()
    c.show()
    sys.exit(app.exec_())