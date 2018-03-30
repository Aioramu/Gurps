import armor
import rand
from random import *
from armor import Bow
from armor import Sword
#kick=Sword.move()
class Knight:
    def __init__(self,weapon_dmg):
        self.weapon_dmg=weapon_dmg
    def Health():
        hp=17
        return hp

    def weapon_dmg():
        dmg = int(Sword.Punch())
        return dmg
        return weapon_dmg
    def weapon_distance():
        distance = 5
        return distance

    def distance():
        distance = randint(1, 10)
        return distance
class Knight2:
    def __init__(self,weapon_dmg):
        self.armor_dmg=weapon_dmg
    def Health():
        hp=17
        return hp
    def weapon_dmg():
        dmg = int(Sword.Punch())
        return dmg
        return weapon_dmg
    def weapon_coldown():
        coldown=Sword.coldown()
        return coldown
    def weapon_distance():
        distance=Sword.weapon_distance()
        return distance
class Archer:
    def __init__(self,weapon_dmg,power):
        self.weapon_dmg=weapon_dmg
        self.power=power
    def Health():
        hp=17
        return hp
    def weapon_dmg():
        dmg=int(Bow.Punch())
        return dmg
    def weapon_coldown():
        coldown=Bow.coldown()
        return coldown
    def weapon_distance():
        distance=Bow.weapon_distance()
        return distance