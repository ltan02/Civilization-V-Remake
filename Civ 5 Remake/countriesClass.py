from tkinter import *
from civilizationClass import *
from unitsClass import *

################################################################
# Countries Class
################################################################


class UnitedStatesofAmerica(Civilization):
    def __init__(self, cities=["Washington", "New York", "Boston", "Philadelphia", "Atlanta"]):
        super().__init__(cities)

    def createSettler(self):
        data.settlers.append(Settler(row, col))


class England(Civilization):
    def __init__(self, cities=["London", "York", "Nottingham", "Hastings", "Canterbury"]):
        super().__init__(cities)


class France(Civilization):
    def __init__(self, cities=["Paris", "Orleans", "Lyon", "Troyes", "Tours"]):
        super().__init__(cities)


class Germany(Civilization):
    def __init__(self, cities=["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt"]):
        super().__init__(cities)
