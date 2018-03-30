import random
from random import *
import pygame

def roll():
    result=randint(1,6)
    return result
def triple_roll():
    result=randint(1,6)+randint(1,6)+randint(1,6)
    return result
#print(triple_roll())
class Archer_parameters:
    def power():
        power=10
        return power
class Knight_parameters:
    def power():
        power=15
        return power
