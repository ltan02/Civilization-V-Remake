from tkinter import *
from civilizationClass import *
from countriesClass import *

################################################################
# Unit Class USA
################################################################


class Unit(UnitedStatesofAmerica):
    def __init__(self, row, col, spawnedCities=[]):
        super().__init__(spawnedCities)
        self.row = row
        self.col = col

    def move(self):
        pass

    def attack(self):
        pass

    def retaliate(self):
        pass

    def draw(self, canvas, data):
        row = self.row
        col = self.col
        xWidth = 46
        yHeight = 91
        hexagonHeight = 61
        hexagonWidth = 50
        if row % 2 == 0:
            startingX = 23
            startingY = -21
            row //= 2
            cx = (xWidth * col) + (hexagonWidth // 2)
            cy = (startingY + (yHeight * row)) + (hexagonHeight // 2)
            canvas.create_rectangle(cx - 10, cy - 15, cx + 10, cy + 15, fill="red")
        else:
            startingX = -23
            startingY = 21
            row //= 2
            cx = startingX + (xWidth * col) + (xWidth // 2)
            cy = startingY + (yHeight * row) + (hexagonHeight // 2)
            canvas.create_rectangle(cx - 10, cy - 15, cx + 10, cy + 15, fill="red")


class Worker(Unit):
    def __init__(self):
        pass

    def build(self):
        pass


class Settler(Unit):
    def __init__(self, row, col, spawnedCities=[], gameStarted=True):
        super().__init__(row, col, spawnedCities)
        self.gameStarted = gameStarted

    def createCity(self, data):
        self.startCity(data, self.row, self.col)
