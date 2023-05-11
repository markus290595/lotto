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
        self._erste = erste
        self._letzte = letzte
        self._ziehungen = ziehungen
        self._lottozahlen = []

        # generate Methode aufrufen
        self.__generate()

    def __generate(self):
        """Methode generiert eine Lottoziehung

        :return: None
        :rtype: None
        """

        for _ in range (0, self._ziehungen):
            self._lottozahlen.append(np.random.randint(self._erste, self._letzte + 1))

    def return_lottozahlen(self):
        """Gibt die gezogenen Lottozahlen zurück
        :return: Lottozahlen einer Ziehung
        :rtype: list
        """

        return self._lottozahlen
    
    def return_mean(self):
        """Gibt den Mittelwert der gezogenen Lottozahlen zurück
        :return: Mittelwert
        :rtype: float
        """

        return np.mean(self._lottozahlen)


class lottozahlen_simulator():

    def __init__(self, erste, letzte, ziehungen, anzahl):
        """Klasse, die mehrere Lottoziehungen simuliert.

        :param erste: erste mögliche Zahl der Ziehung
        :param letzte: letzte mögliche Zahl der Ziehung
        :param ziehungen: Anzahl der Ziehungen in einem Spiel
        :param anzahl: Anzahl der Lottospiele
        """

        # Parameter festlegen
        self._erste = erste
        self._letzte = letzte
        self._ziehungen = ziehungen
        self._anzahl = anzahl
        self._liste_lottozahlen = []

        # generate Methode aufrufen
        self.__generate()

    def __generate(self):
        """Generiert mehrere Lottoziehungen.
        :return: None
        :rtype: None
        """

        for _ in range(0, self._anzahl):
            aktuelle_ziehung = lottozahlen(
                erste = self._erste,
                letzte = self._letzte,
                ziehungen = self._ziehungen
            )

            self._liste_lottozahlen.append(aktuelle_ziehung.return_lottozahlen())

    def return_mean(self):
        """Gibt den Mittelwert der Mittelwerte aller Ziehungen zurück.
        :return: Mittelwert 
        :rtype: float
        """

        mean_liste = []

        for lottozahlen in self._liste_lottozahlen:
            mean_liste.append(np.mean(lottozahlen))

        return np.mean(mean_liste)
    
    def return_liste_lottozahlen(self):
        """Gibt die Liste aller gezogenen Lottozahlen zurück.
        :return: Liste der Lottozahlen aller simulierten Spiele
        :rtype: list
        """
        return self._liste_lottozahlen


