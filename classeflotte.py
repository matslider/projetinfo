import classemobile
import cartebrest
import time
from copy import deepcopy

class Flotte(list):
    """ classe qui réportorie l'inégralité des mobiles et qui gère leur interaction au coup par coup"""
    map_support = cartebrest.map
    import time
    def __init__(self,myflotte=['M'],carte=map_support):
                self.__carte=carte
                for i in range (len(myflotte)):
                    self.append(classemobile.Mobile(1,1))

    def evolute(self):
        for nav in self:
            nav.moove()

    def __str__(self):
        for i in self:
            a=deepcopy(self.__carte)
            x = round(i.get_x())
            y = round(i.get_y())
            a[x, y] = i.id_mobile()
        return str(a)

if __name__ == "__main__":
    Flo = Flotte()
    print(Flo)
    Flo.evolute()
    print(Flo)
