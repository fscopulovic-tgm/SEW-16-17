"""
@author: Filip Scopulovic
@date: 07-11-2016
@use: Model des Spieles, das sich um Statistik kuemmert
"""
from random import Random

class MeinModel:
    """
    Model, das sich um die Statistik gehoert
    """

    def __init__(self):
        """
        Konstruktor der Klasse
        Initialisiert Daten, die fuer das Spiel wichtig sind
        """
        self.__offene_buttons = 15
        self.__korrekt = 0
        self.__falsch = 0
        self.__spiele = 1

    def get_offene_buttons(self):
        """
        Liefert das Attribut __offene_buttons zurueck

        :return int self.__offene_buttons:
        """
        return self.__offene_buttons

    def get_korrekt(self):
        """
        Liefert das Attribut __korrekt zurueck

        :return int self.__korrekt:
        """
        return self.__korrekt

    def get_falsch(self):
        """
        Liefert das Attribut falsch zurueck

        :return int self.__falsch:
        """
        return self.__falsch

    def get_spiele(self):
        """
        Liefert das Attribut __spiele zurueck

        :return int self.__spiele:
        """
        return self.__spiele

    def get_gesamt(self):
        """
        Liefert den Wert von korrekt + falsch

        :return int self.__korrekt + self.__falsch:
        """
        return self.__korrekt + self.__falsch

    def minus_offene_buttons(self):
        """
        Setzt das Attribut __offene_buttons -1

        :return: None
        """
        self.__offene_buttons -= 1

    def plus_korrekt(self):
        """
        Setzt das Attribut __korrekt +1

        :return: None
        """
        self.__korrekt += 1

    def plus_falsch(self):
        """
        Setzt das Attribut __falsch +1

        :return: None
        """
        self.__falsch += 1

    def plus_spiel(self):
        """
        Setzt den Wert __spiel +1

        :return: None
        """
        self.__spiele += 1

    def zuruecksetzen(self):
        """
        Setzt die Werte fuer die Spiele zurueck

        :return: None
        """
        self.__offene_buttons = 15
        self.__korrekt = 0
        self.__falsch = 0