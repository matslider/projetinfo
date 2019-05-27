from math import cos, sin, pi

class Mobile():
    """
    Classe décrivant les comportements par défauts des différents mobiles
    """


    def __init__(self, x = 0, y=0, speed=1, course=150,name='unknown'):
        """Crée un mobile a une position, une vitesse et un cap donné"""

        self.__x = x
        self.__y = y
        self.__speed = speed
        self.__course = course
        self.__name =name

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self,x):
        self.__x = x

    def set_y(self,y):
        self.__y = y


    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y




    def name_mobile(self):
        """ Renvoie l'identifiant du mobile"""
        return 'M'

    def id_mobile(self):
        """Renvoie l'entier ASCII correspondant à l'identifiant du mobile"""
        return ord(Mobile.name_mobile(self))

    def __str__(self):
        """   Affiche l'état courant du mobile    """

        return "%c : position (%i, %i) etat %i/%i" % (
            self.name_mobile(), self.get_x(), self.get_y(), self.speed, self.course)

    def moove(self,t=1):
        """
        Déplace le mobile
        """
        d=self.__speed/t

        self.set_x(self.get_x()+d*sin(self.__course*pi/180))
        self.set_y(self.get_y()- d*cos(self.__course*pi/180))

