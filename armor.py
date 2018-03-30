from rand import *
import Cratures
#from Cratures import *

class Sword():
    def __init__(self, damage, weapon):
        self.damage = damage
        self.weapon = weapon
    def Punch():
        attr={8:randint(1,18)-4,9:randint(1,18)-2,10:randint(1,18)}
        keys=attr.keys()
        keys=sorted(keys)
        power = Archer_parameters.power()
        for key in keys:
            if key==power:
                weapon=attr[key]
                break
        if weapon <= 0:
            weapon = 0
        return weapon

    def coldown():
        coldown = 0
        return coldown

    def weapon_distance():
        distance = 1
        return distance


class Bow():
    def __init__(self,damage,weapon):
        self.damage=damage
        self.weapon=weapon

    def Punch():
        attr={8:randint(1,18)-4,9:randint(1,18)-2,10:randint(1,18)}
        keys=attr.keys()
        keys=sorted(keys)
        power = Archer_parameters.power()
        for key in keys:
            if key==power:
                weapon=attr[key]
                break
        if weapon <= 0:
            weapon = 0
        return weapon

        #return weapon_dmg
    def coldown():
        coldown=2
        return coldown
    def weapon_distance():
        distance = 5
        return distance
