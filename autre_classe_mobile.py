class Moteur(Mobile):

    def __init__(self, abscisse, ordonnee, speed, course, fuel, capacite):
        self.__niveau = randint(capacite // 2, capacite)
        self._reservoir = capacite
        self._fuel = max(fuel, capacite)

    @property
    def fuel(self):
        """
        renvoie le niveau de fuel
        """
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        """
        Met à jour le niveau de fuel de carburant du mobile motorisé
        """
        if value <= self._max:
            self.__sante = value
        if value <= 0:  # <= car certaines cases enlèvent plus de 1 en santé
            value = 0  # ce qui gèrera les décès plus tard

    def plein(self):
        """
        fait le plein de carburant"
        """
        self.fuel = self._max

    class Pecheur(Moteur):

        def car(self):
            return 'P'

    class Passagers(Moteur):

        class Ouessant(Passagers):

        class Transrade(Passagers):

            def car(self):
                return 'T'

    class Commerce(Moteur):

    class Militaire(Moteur):

        class Surface(Militaire):

        class Sous_marin():

    class Plaisance():


class Non_moteur(Mobile):
    class Voile(Non_moteur):

    class Banc(Non_moteur):

    class polution(Non_moteur):