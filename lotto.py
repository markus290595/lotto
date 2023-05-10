import numpy as np
import matplotlib.pyplot as plt


class lottozahlen():
    
    def __init__(self, erste, letzte, ziehungen):
        """Klasse, die eine Lottoziehung simuliert.

        :param erste: erste mögliche Zahl der Ziehung
        :param letzte: letzte mögliche Zahl der Ziehung
        :param ziehungen: Anzahl der Ziehungen in einem Spiel
        """

        # Parameter festlegen
        self.__erste = erste
        self.__letzte = letzte
        self.__ziehungen = ziehungen
        self.__lottozahlen = []

        # generate Methode aufrufen
        self.__generate()

    def __generate(self):
        """Methode generiert eine Lottoziehung

        :return: None
        :rtype: None
        """

        for _ in range (0, self.__ziehungen):
            self.__lottozahlen.append(np.random.randint(self.__erste, self.__letzte + 1))

    def return_lottozahlen(self):
        """Gibt die gezogenen Lottozahlen zurück
        :return: Lottozahlen einer Ziehung
        :rtype: list
        """

        return self.__lottozahlen
    
    def return_mean(self):
        """Gibt den Mittelwert der gezogenen Lottozahlen zurück
        :return: Mittelwert
        :rtype: float
        """

        return np.mean(self.__lottozahlen)


class lottozahlen_simulator():

    def __init__(self, erste, letzte, ziehungen, anzahl):
        """Klasse, die mehrere Lottoziehungen simuliert.

        :param erste: erste mögliche Zahl der Ziehung
        :param letzte: letzte mögliche Zahl der Ziehung
        :param ziehungen: Anzahl der Ziehungen in einem Spiel
        :param anzahl: Anzahl der Lottospiele
        """

        # Parameter festlegen
        self.__erste = erste
        self.__letzte = letzte
        self.__ziehungen = ziehungen
        self.__anzahl = anzahl
        self.__liste_lottozahlen = []

        # generate Methode aufrufen
        self.__generate()

    def __generate(self):
        """Generiert mehrere Lottoziehungen.
        :return: None
        :rtype: None
        """

        for _ in range(0, self.__anzahl + 1):
            aktuelle_ziehung = lottozahlen(
                erste = self.__erste,
                letzte = self.__letzte,
                ziehungen = self.__ziehungen
            )

            self.__liste_lottozahlen.append(aktuelle_ziehung.return_lottozahlen())

    def return_mean(self):
        """Gibt den Mittelwert der Mittelwerte aller Ziehungen zurück.
        :return: Mittelwert 
        :rtype: float
        """

        mean_liste = []

        for lottozahlen in self.__liste_lottozahlen:
            mean_liste.append(np.mean(lottozahlen))

        return np.mean(mean_liste)
    
    def return_liste_lottozahlen(self):
        """Gibt die Liste aller gezogenen Lottozahlen zurück.
        :return: Liste der Lottozahlen aller simulierten Spiele
        :rtype: list
        """
        return self.__liste_lottozahlen


