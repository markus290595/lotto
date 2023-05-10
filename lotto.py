import numpy as np
import matplotlib.pyplot as plt


class lottozahlen():
    
    def __init__(self, erste, letzte, ziehungen):
        self.__erste = erste
        self.__letzte = letzte
        self.__ziehungen = ziehungen
        self.__lottozahlen = []

        self.__generate()

    def __generate(self):

        for _ in range (0, self.__ziehungen):
            self.__lottozahlen.append(np.random.randint(self.__erste, self.__letzte + 1))

    def return_lottozahlen(self):

        return self.__lottozahlen
    
    def return_mean(self):

        return np.mean(self.__lottozahlen)


class lottozahlen_simulator():

    def __init__(self, erste, letzte, ziehungen, anzahl):
        self.__erste = erste
        self.__letzte = letzte
        self.__ziehungen = ziehungen
        self.__anzahl = anzahl
        self.__liste_lottozahlen = []

        self.__generate()

    def __generate(self):

        for _ in range(0, self.__anzahl + 1):

            aktuelle_ziehung = lottozahlen(
                erste = self.__erste,
                letzte = self.__letzte,
                ziehungen = self.__ziehungen
            )

            self.__liste_lottozahlen.append(aktuelle_ziehung.return_lottozahlen())

    def return_mean(self):

        mean_liste = []

        for lottozahlen in self.__liste_lottozahlen:

            mean_liste.append(np.mean(lottozahlen))

        return np.mean(mean_liste)
    
    def return_liste_lottozahlen(self):

        return self.__liste_lottozahlen


lotto = lottozahlen_simulator(
    erste = 1,
    letzte = 46,
    ziehungen = 6, 
    anzahl = 1000
)

print(lotto.return_liste_lottozahlen())
print(lotto.return_mean())


