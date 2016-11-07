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

        self.myForm = MyView.Ui_Spiel()
        self.myForm.setupUi(self)
        self.__model = MyModel.MeinModel()

        #Vorhanden ist eine Liste mit den schon vorhanden Zahlen
        self.__vorhanden = []

        #Dieser Abschnitt ist dafuer da, die Zahlbuttons aus der View zu bekommen
        self.__buttons = []
        for i in range(15):
            #Mit Format werden die Namen der Buttons initialisiert
            gewaehlter_button = "zahl_{0}".format(i)
            #Mit getattr werden die Buttons zurueckgeliefert
            zahl_button = getattr(self.__view, gewaehlter_button)
            #Man addet die Buttons in eine Liste
            self.__buttons.append(zahl_button)

        #Dieser Abschnitt kuemmert sich darum, das die Buttons mit ihren Methoden verbinden werden
        self.__view.neustart.clicked.connect(self.__spiel_neustarten)
        #Ich wusste nicht wie man die Buttons mit einer For-Schleife mit einem Signal verbindet,
        # also habe ich den Schüler Pierre Rieger gefragt und er hat mir dann durch seine Hilfe die for-Schleife erklärt
        for b in self.__buttons:
            b.clicked.connect(lambda b=b: self.__zahl_button_geklickt(b))

        self.start()

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

        :return: None
        """
        geklickter_button = int(btn.text())
        if geklickter_button == self.__vorhanden:
            btn.setEnable(False)
            self.__model.minus_offene_buttons()
            self.__model.plus_korrekt()
            self.__vorhanden.pop(geklickter_button)
        else:
            self.__model.plus_falsch()
        self.__labels_updaten()

    def __labels_updaten(self):
        """
        Aktualisiert die Labels mit neuen Werten

        :return: None
        """
        self.__view.offen_zaehler.setText(str(self.__model.get_offene_buttons))
        self.__view.korrekt_zaehler.setText(str(self.__model.get_korrekt))
        self.__view.falsch_zaehler.setText(str(self.__model.get_falsch))
        self.__view.gesamt_zaehler.setText(str(self.__model.get_gesamt))
        self.__view.spiel_zaehler.setText(str(self.__model.get_spiele))

    def __set_zahl_button(self):
        """
        Setzt den Text

        :return: None
        """
        zufall = Random()
        nichtvorhanden = []
        for i in range(0, 16):
            nichtvorhanden.append(i)

        for b in self.__buttons:
            zufall_index = zufall.randint(0, len(nichtvorhanden))
            self.__vorhanden.append(zufall_index)
            nichtvorhanden.pop(zufall_index)

        self.__vorhanden.sort()

if __name__ == "__main__":
    app = QtCore.QApplication(sys.argv)
    c = MeinKontroller()
    c.show()
    sys.exit(app.exec_())