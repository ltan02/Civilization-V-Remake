from tkinter import *
import random


def drawTiles(canvas, data, row, col):
    if row % 2 == 1:
        cityTiles = [(row - 1, col - 1), (row - 1, col), (row, col - 1), (row, col), (row, col + 1), (row + 1, col - 1), (row + 1, col)]
    else:
        cityTiles = [(row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col), (row, col + 1), (row + 1, col), (row + 1, col + 1)]
    for eachTile in cityTiles:
        xWidth = 46
        yHeight = 91
        hexagonHeight = 59
        hexagonWidth = 50
        row, col = eachTile[0], eachTile[1]
        if row % 2 == 0:
            startingX = 25
            startingY = -24
            row //= 2
            cx = (xWidth * col) + (hexagonWidth // 2)
            cy = (startingY + (yHeight * row)) + (hexagonHeight // 2)
        else:
            startingX = -25
            startingY = 24
            row //= 2
            cx = startingX + (xWidth * col) + (xWidth // 2)
            cy = startingY + (yHeight * row) + (hexagonHeight // 2)
        canvas.create_polygon(cx, cy - 27, cx + 23, cy - 12, cx + 23, cy + 20, cx, cy + 35, cx - 23, cy + 20, cx - 23, cy - 12, fill="", outline="red", width=3)


################################################################
# Unit Class
################################################################


class Unit(object):
    def __init__(self, country, moves, defaultMoves, selected, row, col, name, color, damage, health):
        self.country = country
        self.defaultMoves = defaultMoves
        self.moves = moves
        self.selected = selected
        self.row = row
        self.col = col
        self.color = color
        self.selectedColor = color
        self.damage = damage
        self.health = health
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        else:
            return self.name == other.name

    def retaliate(self, other, data):
        other.health -= self.damage * 0.5
        other.health = int(other.health)

        if other.health < 0:
            other.health = 0

        if other.health == 0:
            if other.country == "usa":
                for eachUnit in data.usaUnits:
                    if eachUnit[0] == other.name and eachUnit[0].health == 0:
                        data.usaUnits.remove(eachUnit)
            elif other.country == "uk":
                for eachUnit in data.ukUnits:
                    if eachUnit[0] == other.name and eachUnit[0].health == 0:
                        data.ukUnits.remove(eachUnit)
            elif other.country == "french":
                for eachUnit in data.frenchUnits:
                    if eachUnit[0] == other.name and eachUnit[0].health == 0:
                        data.frenchUnits.remove(eachUnit)
            else:
                for eachUnit in data.germanUnits:
                    if eachUnit[0] == other.name and eachUnit[0].health == 0:
                        data.germanUnits.remove(eachUnit)

    def getColor(self):
        if self.color == None:
            if self.country == "usa":
                self.color = "red"
            elif self.country == "uk":
                self.color = "orange"
            elif self.country == "french":
                self.color = "DarkOliveGreen3"
            else:
                self.color = "black"

    def possibleMoves(self):
        if self.moves == 0:
            return []

        if self.moves == 1:
            if self.row % 2 == 0:
                return [(self.row - 1, self.col), (self.row - 1, self.col + 1), (self.row, self.col - 1), (self.row, self.col),
                        (self.row, self.col + 1), (self.row + 1, self.col), (self.row + 1, self.col + 1)]
            else:
                return [(self.row - 1, self.col - 1), (self.row - 1, self.col), (self.row, self.col - 1), (self.row, self.col),
                        (self.row, self.col + 1), (self.row + 1, self.col - 1), (self.row + 1, self.col)]

        if self.moves == 2:
            if self.row % 2 == 0:
                return [(self.row - 2, self.col - 1), (self.row - 2, self.col), (self.row - 2, self.col + 1), (self.row - 1, self.col - 1),
                        (self.row - 1, self.col), (self.row - 1, self.col + 1), (self.row - 1, self.col + 2), (self.row, self.col - 2),
                        (self.row, self.col - 1), (self.row, self.col), (self.row, self.col + 1), (self.row, self.col + 2),
                        (self.row + 1, self.col - 1), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2),
                        (self.row + 2, self.col - 1), (self.row + 2, self.col), (self.row + 2, self.col + 1)]
            else:
                return [(self.row - 2, self.col - 1), (self.row - 2, self.col), (self.row - 2, self.col + 1), (self.row - 1, self.col - 2),
                        (self.row - 1, self.col - 1), (self.row - 1, self.col), (self.row - 1, self.col + 1), (self.row, self.col - 2),
                        (self.row, self.col - 1), (self.row, self.col), (self.row, self.col + 1), (self.row, self.col + 2),
                        (self.row + 1, self.col - 2), (self.row + 1, self.col - 1), (self.row + 1, self.col), (self.row + 1, self.col + 1),
                        (self.row + 2, self.col - 1), (self.row + 2, self.col), (self.row + 2, self.col + 1)]
        return []

    def clicked(self, data, rowClicked, colClicked):
        if self.country == "usa":
            for eachUnit in data.usaUnits:
                row, col = eachUnit[1][0], eachUnit[1][1]
                if row == rowClicked and col == colClicked:
                    return True
            return False
        elif self.country == "uk":
            for eachUnit in data.ukUnits:
                row, col = eachUnit[1][0], eachUnit[1][1]
                if row == rowClicked and col == colClicked:
                    return True
            return False
        elif self.country == "french":
            for eachUnit in data.frenchUnits:
                row, col = eachUnit[1][0], eachUnit[1][1]
                if row == rowClicked and col == colClicked:
                    return True
            return False
        else:
            for eachUnit in data.germanUnits:
                row, col = eachUnit[1][0], eachUnit[1][1]
                if row == rowClicked and col == colClicked:
                    return True
            return False

    def drawMoveTiles(self, canvas, data, row, col):
        if self.selected and not(isinstance(self, City)):
            cityTiles = self.possibleMoves()
            for eachTile in cityTiles:
                xWidth = 46
                yHeight = 91
                hexagonHeight = 59
                hexagonWidth = 50
                row, col = eachTile[0], eachTile[1]
                if row % 2 == 0:
                    startingX = 25
                    startingY = -24
                    row //= 2
                    cx = (xWidth * col) + (hexagonWidth // 2)
                    cy = (startingY + (yHeight * row)) + (hexagonHeight // 2)
                else:
                    startingX = -25
                    startingY = 24
                    row //= 2
                    cx = startingX + (xWidth * col) + (xWidth // 2)
                    cy = startingY + (yHeight * row) + (hexagonHeight // 2)
                canvas.create_polygon(cx, cy - 27, cx + 23, cy - 12, cx + 23, cy + 20, cx, cy + 35, cx - 23, cy + 20, cx - 23, cy - 12, fill="", outline="deep pink", width=3)


################################################################
# Support Unit
################################################################


class Support(Unit):
    def __init__(self, row, col, country, moves, defaultMoves, selected, name, color, damage, health):
        super().__init__(country, moves, defaultMoves, selected, row, col, name, color, damage, health)

class Worker(Support):
    def __init__(self, row, col, country, moves=1, defaultMoves=1, selected=False, name="worker", color=None, damage=0, health=30):
        super().__init__(row, col, country, moves, defaultMoves, selected, name, color, damage, health)

    def build(self):
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
            canvas.create_rectangle(cx - 10, cy - 15, cx + 10, cy + 15, fill=self.color, outline="PaleTurquoise1", width=5)
            canvas.create_text(cx, cy, text=self.health, font="ComicSansMS 10", fill="white")
        else:
            startingX = -23
            startingY = 21
            row //= 2
            cx = startingX + (xWidth * col) + (xWidth // 2)
            cy = startingY + (yHeight * row) + (hexagonHeight // 2)
            canvas.create_rectangle(cx - 10, cy - 15, cx + 10, cy + 15, fill=self.color, outline="PaleTurquoise1", width=5)
            canvas.create_text(cx, cy, text=self.health, font="ComicSansMS 10", fill="white")

    def increaseProduction(self):
        pass


class Settler(Support):
    def __init__(self, row, col, country, moves=1, defaultMoves=1, selected=False, name="settler", color=None, damage=0, health=30):
        super().__init__(row, col, country, moves, defaultMoves, selected, name, color, damage, health)

    def startingSettler(self, data):
        if data.gameStarted:
            row, col = getRowAndCol(data)
            data.settlers.append([self.country, (row, col)])

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
            canvas.create_rectangle(cx - 10, cy - 15, cx + 10, cy + 15, fill=self.color, outline="MediumOrchid1", width=5)
            canvas.create_text(cx, cy, text=self.health, font="ComicSansMS 10", fill="white")
        else:
            startingX = -23
            startingY = 21
            row //= 2
            cx = startingX + (xWidth * col) + (xWidth // 2)
            cy = startingY + (yHeight * row) + (hexagonHeight // 2)
            canvas.create_rectangle(cx - 10, cy - 15, cx + 10, cy + 15, fill=self.color, outline="MediumOrchid1", width=5)
            canvas.create_text(cx, cy, text=self.health, font="ComicSansMS 10", fill="white")

    def removeSelf(self, data):
        if self.country == "usa":
            for units in data.usaUnits:
                if units[0] == "settler":
                    index = data.usaUnits.index(units)
                    data.usaUnits[index] = [City(data.usaTempCity[0], data.usaTempCity[1][0], data.usaTempCity[1][1]), (self.row, self.col)]
                break
        elif self.country == "uk":
            for units in data.ukUnits:
                if units[0] == "settler":
                    index = data.ukUnits.index(units)
                    data.ukUnits[index] = [City(data.ukTempCity[0], data.ukTempCity[1][0], data.ukTempCity[1][1]), (self.row, self.col)]
                break
        elif self.country == "french":
            for units in data.frenchUnits:
                if units[0] == "settler":
                    index = data.frenchUnits.index(units)
                    data.frenchUnits[index] = [City(data.frenchTempCity[0], data.frenchTempCity[1][0], data.frenchTempCity[1][1]),
                                               (self.row, self.col)]
                break
        else:
            for units in data.germanUnits:
                if units[0] == "settler":
                    index = data.germanUnits.index(units)
                    data.germanUnits[index] = [City(data.germanTempCity[0], data.germanTempCity[1][0], data.germanTempCity[1][1]),
                                               (self.row, self.col)]
                break

        data.usaTempCity = []
        data.ukTempCity = []
        data.frenchTempCity = []
        data.germanTempCity = []

    def createCity(self, data):
        if self.country == "usa":
            tmp = data.usaCities.pop(0)
            data.usaTempCity = [tmp, (self.row, self.col)]
            data.usaSpawnedCities.append([tmp, (self.row, self.col)])
        elif self.country == "uk":
            tmp = data.ukCities.pop(0)
            data.ukTempCity = [tmp, (self.row, self.col)]
            data.ukSpawnedCities.append([tmp, (self.row, self.col)])
        elif self.country == "french":
            tmp = data.frenchCities.pop(0)
            data.frenchTempCity = [tmp, (self.row, self.col)]
            data.frenchSpawnedCities.append([tmp, (self.row, self.col)])
        elif self.country == "germany":
            tmp = data.germanCities.pop(0)
            data.germanTempCity = [tmp, (self.row, self.col)]
            data.germanSpawnedCities.append([tmp, (self.row, self.col)])
        self.removeSelf(data)

    def drawCity(self, canvas, data):
        if self.country == "usa":
            for city in data.usaSpawnedCities:
                row, col = city[1][0], city[1][1]
                drawTiles(canvas, data, row, col)
        elif self.country == "uk":
            for city in data.ukSpawnedCities:
                row, col = city[1][0], city[1][1]
                drawTiles(canvas, data, row, col)
        elif self.country == "french":
            for city in data.frenchSpawnedCities:
                row, col = city[1][0], city[1][1]
                drawTiles(canvas, data, row, col)
        else:
            for city in data.germanSpawnedCities:
                row, col = city[1][0], city[1][1]
                drawTiles(canvas, data, row, col)

################################################################
# City Unit
################################################################


class City(Unit):
    def __init__(self, name, row, col, health=250, production=10, selected=False, color=None, damage=50):
        self.name = name
        self.row = row
        self.col = col
        self.health = health
        self.production = production
        self.selected = selected
        self.country = None
        self.type = "City"
        self.color = color
        self.damage = damage

    def __repr__(self):
        return self.type

    def __eq__(self, other):
        return isinstance(other, str) and self.type == other

    def getCountry(self, data):
        if self.country == None:
            if self.name in data.usaCitiesUnchanged:
                self.country = "usa"
            elif self.name in data.ukCitiesUnchanged:
                self.country = "uk"
            elif self.name in data.frenchCitiesUnchanged:
                self.country = "french"
            else:
                self.country = "germany"

    def getColor(self):
        if self.color == None:
            if self.country == "usa":
                self.color = "red"
            elif self.country == "uk":
                self.color = "orange"
            elif self.country == "french":
                self.color = "DarkOliveGreen3"
            elif self.country == "germany":
                self.color = "black"

    def draw(self, canvas, data):
        row = self.row
        col = self.col
        self.getColor()
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
            canvas.create_rectangle(cx - 10, cy - 10, cx + 10, cy + 10, fill=self.color)
            canvas.create_text(cx, cy, text=self.health, font="ComicSansMS 10", fill="white")
        else:
            startingX = -23
            startingY = 21
            row //= 2
            cx = startingX + (xWidth * col) + (xWidth // 2)
            cy = startingY + (yHeight * row) + (hexagonHeight // 2)
            canvas.create_rectangle(cx - 10, cy - 10, cx + 10, cy + 10, fill=self.color)
            canvas.create_text(cx, cy, text=self.health, font="ComicSansMS 10", fill="white")

    def drawCity(self, canvas, data):
        drawTiles(canvas, data, self.row, self.col)

    def createWorker(self, data):
        if self.selected:
            newRow, newCol = self.row, self.col - 1
            if data.board[newRow][newCol] in [2, 5, 6]:
                newRow, newCol = self.row, self.col + 1
            if data.board[newRow][newCol] in [2, 5, 6]:
                newRow, newCol = self.row + 1, self.col
            if data.board[newRow][newCol] in [2, 5, 6]:
                newRow, newCol = self.row - 1, self.col

            if self.country == "usa":
                data.usaUnits.append([Worker(newRow, newCol, self.country, 0), (newRow, newCol)])
            elif self.country == "uk":
                data.ukUnits.append([Worker(newRow, newCol, self.country, 0), (newRow, newCol)])
            elif self.country == "french":
                data.frenchUnits.append([Worker(newRow, newCol, self.country, 0), (newRow, newCol)])
            else:
                data.germanUnits.append([Worker(newRow, newCol, self.country, 0), (newRow, newCol)])
            self.production += 1

    def createWarrior(self, data):
        if self.selected:
            newRow, newCol = self.row, self.col - 1
            if data.board[newRow][newCol] in [2, 5, 6]:
                newRow, newCol = self.row, self.col + 1
            if data.board[newRow][newCol] in [2, 5, 6]:
                newRow, newCol = self.row + 1, self.col
            if data.board[newRow][newCol] in [2, 5, 6]:
                newRow, newCol = self.row - 1, self.col

            if self.country == "usa":
                data.usaUnits.append([Warrior(newRow, newCol, self.country, 0), (newRow, newCol)])
            elif self.country == "uk":
                data.ukUnits.append([Warrior(newRow, newCol, self.country, 0), (newRow, newCol)])
            elif self.country == "french":
                data.frenchUnits.append([Warrior(newRow, newCol, self.country, 0), (newRow, newCol)])
            else:
                data.germanUnits.append([Warrior(newRow, newCol, self.country, 0), (newRow, newCol)])

    def createSwordsman(self, data):
        if self.selected:
            newRow, newCol = self.row, self.col - 1
            if data.board[newRow][newCol] in [2, 5, 6]:
                newRow, newCol = self.row, self.col + 1
            if data.board[newRow][newCol] in [2, 5, 6]:
                newRow, newCol = self.row + 1, self.col
            if data.board[newRow][newCol] in [2, 5, 6]:
                newRow, newCol = self.row - 1, self.col

            if self.country == "usa":
                data.usaUnits.append([Swordsman(newRow, newCol, self.country, 0), (newRow, newCol)])
            elif self.country == "uk":
                data.ukUnits.append([Swordsman(newRow, newCol, self.country, 0), (newRow, newCol)])
            elif self.country == "french":
                data.frenchUnits.append([Swordsman(newRow, newCol, self.country, 0), (newRow, newCol)])
            else:
                data.germanUnits.append([Swordsman(newRow, newCol, self.country, 0), (newRow, newCol)])

    def createArcher(self, data):
        if self.selected:
            newRow, newCol = self.row, self.col - 1
            if data.board[newRow][newCol] in [2, 5, 6]:
                newRow, newCol = self.row, self.col + 1
            if data.board[newRow][newCol] in [2, 5, 6]:
                newRow, newCol = self.row + 1, self.col
            if data.board[newRow][newCol] in [2, 5, 6]:
                newRow, newCol = self.row - 1, self.col

            if self.country == "usa":
                data.usaUnits.append([Archer(newRow, newCol, self.country, 0), (newRow, newCol)])
            elif self.country == "uk":
                data.ukUnits.append([Archer(newRow, newCol, self.country, 0), (newRow, newCol)])
            elif self.country == "french":
                data.frenchUnits.append([Archer(newRow, newCol, self.country, 0), (newRow, newCol)])
            else:
                data.germanUnits.append([Archer(newRow, newCol, self.country, 0), (newRow, newCol)])

    def aicreateSettler(self, data):
        newRow, newCol = self.row, self.col - 1
        if data.board[newRow][newCol] in [2, 5, 6]:
            newRow, newCol = self.row, self.col + 1
        if data.board[newRow][newCol] in [2, 5, 6]:
            newRow, newCol = self.row + 1, self.col
        if data.board[newRow][newCol] in [2, 5, 6]:
            newRow, newCol = self.row - 1, self.col

        if self.country == "usa":
            data.usaUnits.append([Settler(newRow, newCol, self.country, 0), (newRow, newCol)])
        elif self.country == "uk":
            data.ukUnits.append([Settler(newRow, newCol, self.country, 0), (newRow, newCol)])
        elif self.country == "french":
            data.frenchUnits.append([Settler(newRow, newCol, self.country, 0), (newRow, newCol)])
        else:
            data.germanUnits.append([Settler(newRow, newCol, self.country, 0), (newRow, newCol)])

    def aicreateWorker(self, data):
        newRow, newCol = self.row, self.col - 1
        if data.board[newRow][newCol] in [2, 5, 6]:
            newRow, newCol = self.row, self.col + 1
        if data.board[newRow][newCol] in [2, 5, 6]:
            newRow, newCol = self.row + 1, self.col
        if data.board[newRow][newCol] in [2, 5, 6]:
            newRow, newCol = self.row - 1, self.col

        if self.country == "usa":
            data.usaUnits.append([Worker(newRow, newCol, self.country, 0), (newRow, newCol)])
        elif self.country == "uk":
            data.ukUnits.append([Worker(newRow, newCol, self.country, 0), (newRow, newCol)])
        elif self.country == "french":
            data.frenchUnits.append([Worker(newRow, newCol, self.country, 0), (newRow, newCol)])
        else:
            data.germanUnits.append([Worker(newRow, newCol, self.country, 0), (newRow, newCol)])
        self.production += 1

    def aicreateWarrior(self, data):
        newRow, newCol = self.row, self.col - 1
        if data.board[newRow][newCol] in [2, 5, 6]:
            newRow, newCol = self.row, self.col + 1
        if data.board[newRow][newCol] in [2, 5, 6]:
            newRow, newCol = self.row + 1, self.col
        if data.board[newRow][newCol] in [2, 5, 6]:
            newRow, newCol = self.row - 1, self.col

        if self.country == "usa":
            data.usaUnits.append([Warrior(newRow, newCol, self.country, 0), (newRow, newCol)])
        elif self.country == "uk":
            data.ukUnits.append([Warrior(newRow, newCol, self.country, 0), (newRow, newCol)])
        elif self.country == "french":
            data.frenchUnits.append([Warrior(newRow, newCol, self.country, 0), (newRow, newCol)])
        else:
            data.germanUnits.append([Warrior(newRow, newCol, self.country, 0), (newRow, newCol)])

    def aicreateSwordsman(self, data):
        newRow, newCol = self.row, self.col - 1
        if data.board[newRow][newCol] in [2, 5, 6]:
            newRow, newCol = self.row, self.col + 1
        if data.board[newRow][newCol] in [2, 5, 6]:
            newRow, newCol = self.row + 1, self.col
        if data.board[newRow][newCol] in [2, 5, 6]:
            newRow, newCol = self.row - 1, self.col

        if self.country == "usa":
            data.usaUnits.append([Swordsman(newRow, newCol, self.country, 0), (newRow, newCol)])
        elif self.country == "uk":
            data.ukUnits.append([Swordsman(newRow, newCol, self.country, 0), (newRow, newCol)])
        elif self.country == "french":
            data.frenchUnits.append([Swordsman(newRow, newCol, self.country, 0), (newRow, newCol)])
        else:
            data.germanUnits.append([Swordsman(newRow, newCol, self.country, 0), (newRow, newCol)])

    def aicreateArcher(self, data):
        newRow, newCol = self.row, self.col - 1
        if data.board[newRow][newCol] in [2, 5, 6]:
            newRow, newCol = self.row, self.col + 1
        if data.board[newRow][newCol] in [2, 5, 6]:
            newRow, newCol = self.row + 1, self.col
        if data.board[newRow][newCol] in [2, 5, 6]:
            newRow, newCol = self.row - 1, self.col

        if self.country == "usa":
            data.usaUnits.append([Archer(newRow, newCol, self.country, 0), (newRow, newCol)])
        elif self.country == "uk":
            data.ukUnits.append([Archer(newRow, newCol, self.country, 0), (newRow, newCol)])
        elif self.country == "french":
            data.frenchUnits.append([Archer(newRow, newCol, self.country, 0), (newRow, newCol)])
        else:
            data.germanUnits.append([Archer(newRow, newCol, self.country, 0), (newRow, newCol)])

    def aicreateSettler(self, data):
        newRow, newCol = self.row, self.col - 1
        if data.board[newRow][newCol] in [2, 5, 6]:
            newRow, newCol = self.row, self.col + 1
        if data.board[newRow][newCol] in [2, 5, 6]:
            newRow, newCol = self.row + 1, self.col
        if data.board[newRow][newCol] in [2, 5, 6]:
            newRow, newCol = self.row - 1, self.col

        if self.country == "usa":
            data.usaUnits.append([Settler(newRow, newCol, self.country, 0), (newRow, newCol)])
        elif self.country == "uk":
            data.ukUnits.append([Settler(newRow, newCol, self.country, 0), (newRow, newCol)])
        elif self.country == "french":
            data.frenchUnits.append([Settler(newRow, newCol, self.country, 0), (newRow, newCol)])
        else:
            data.germanUnits.append([Settler(newRow, newCol, self.country, 0), (newRow, newCol)])


################################################################
# Land Unit
################################################################


class Land(Unit):
    def __init__(self, row, col, country, moves, defaultMoves, selected, name, color, damage, health):
        super().__init__(country, moves, defaultMoves, selected, row, col, name, color, damage, health)

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, str) and self.name == other

    def attack(self, other, data):
        other.health -= self.damage

        if other.health < 0:
            other.health = 0

        if other.health == 0:
            if other.country == "usa":
                for eachUnit in data.usaUnits:
                    if eachUnit[0] == other.name and eachUnit[0].health == 0:
                        data.usaUnits.remove(eachUnit)
            elif other.country == "uk":
                for eachUnit in data.ukUnits:
                    if eachUnit[0] == other.name and eachUnit[0].health == 0:
                        data.ukUnits.remove(eachUnit)
            elif other.country == "french":
                for eachUnit in data.frenchUnits:
                    if eachUnit[0] == other.name and eachUnit[0].health == 0:
                        data.frenchUnits.remove(eachUnit)
            else:
                for eachUnit in data.germanUnits:
                    if eachUnit[0] == other.name and eachUnit[0].health == 0:
                        data.germanUnits.remove(eachUnit)

        self.moves = 0

    def retaliate(self, other):
        other.health -= self.damage * 0.5


class Warrior(Land):
    def __init__(self, row, col, country, moves=2, defaultMoves=2, selected=False, name="warrior", color=None, damage=30, health=80):
        super().__init__(row, col, country, moves, defaultMoves, selected, name, color, damage, health)

    def possibleAttacks(self):
        if self.row % 2 == 0:
            return [(self.row - 1, self.col), (self.row - 1, self.col + 1), (self.row, self.col - 1), (self.row, self.col),
                    (self.row, self.col + 1), (self.row + 1, self.col), (self.row + 1, self.col + 1)]
        else:
            return [(self.row - 1, self.col - 1), (self.row - 1, self.col), (self.row, self.col - 1), (self.row, self.col),
                    (self.row, self.col + 1), (self.row + 1, self.col - 1), (self.row + 1, self.col)]

    def draw(self, canvas, data):
        row = self.row
        col = self.col
        self.getColor()
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
            canvas.create_rectangle(cx - 10, cy - 15, cx + 10, cy + 15, fill=self.color, outline="brown4", width=5)
            canvas.create_text(cx, cy, text=self.health, font="ComicSansMS 10", fill="white")
        else:
            startingX = -23
            startingY = 21
            row //= 2
            cx = startingX + (xWidth * col) + (xWidth // 2)
            cy = startingY + (yHeight * row) + (hexagonHeight // 2)
            canvas.create_rectangle(cx - 10, cy - 15, cx + 10, cy + 15, fill=self.color, outline="brown4", width=5)
            canvas.create_text(cx, cy, text=self.health, font="ComicSansMS 10", fill="white")

class Swordsman(Land):
    def __init__(self, row, col, country, moves=2, defaultMoves=2, selected=False, name="swordsman", color=None, damage=40, health=100):
        super().__init__(row, col, country, moves, defaultMoves, selected, name, color, damage, health)

    def possibleAttacks(self):
        if self.row % 2 == 0:
            return [(self.row - 1, self.col), (self.row - 1, self.col + 1), (self.row, self.col - 1), (self.row, self.col),
                    (self.row, self.col + 1), (self.row + 1, self.col), (self.row + 1, self.col + 1)]
        else:
            return [(self.row - 1, self.col - 1), (self.row - 1, self.col), (self.row, self.col - 1), (self.row, self.col),
                    (self.row, self.col + 1), (self.row + 1, self.col - 1), (self.row + 1, self.col)]

    def draw(self, canvas, data):
        row = self.row
        col = self.col
        self.getColor()
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
            canvas.create_rectangle(cx - 10, cy - 15, cx + 10, cy + 15, fill=self.color, outline="powder blue", width=5)
            canvas.create_text(cx, cy, text=self.health, font="ComicSansMS 10", fill="white")
        else:
            startingX = -23
            startingY = 21
            row //= 2
            cx = startingX + (xWidth * col) + (xWidth // 2)
            cy = startingY + (yHeight * row) + (hexagonHeight // 2)
            canvas.create_rectangle(cx - 10, cy - 15, cx + 10, cy + 15, fill=self.color, outline="powder blue", width=5)
            canvas.create_text(cx, cy, text=self.health, font="ComicSansMS 10", fill="white")


class Ranged(Unit):
    def __init__(self, row, col, country, moves, defaultMoves, selected, name, color, damage, health):
        super().__init__(country, moves, defaultMoves, selected, row, col, name, color, damage, health)

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, str) and self.name == other

    def attack(self, other, data):
        other.health -= self.damage

        if other.health < 0:
            other.health = 0

        if other.health == 0:
            if other.country == "usa":
                for eachUnit in data.usaUnits:
                    if eachUnit[0] == other.name and eachUnit[0].health == 0:
                        data.usaUnits.remove(eachUnit)
            elif other.country == "uk":
                for eachUnit in data.ukUnits:
                    if eachUnit[0] == other.name and eachUnit[0].health == 0:
                        data.ukUnits.remove(eachUnit)
            elif other.country == "french":
                for eachUnit in data.frenchUnits:
                    if eachUnit[0] == other.name and eachUnit[0].health == 0:
                        data.frenchUnits.remove(eachUnit)
            else:
                for eachUnit in data.germanUnits:
                    if eachUnit[0] == other.name and eachUnit[0].health == 0:
                        data.germanUnits.remove(eachUnit)

        self.moves = 0

    def retaliate(self, other):
        other.health -= self.damage * 0.5

    def possibleAttacks(self):
        if self.row % 2 == 0:
            return [(self.row - 2, self.col - 1), (self.row - 2, self.col), (self.row - 2, self.col + 1), (self.row - 1, self.col - 1),
                    (self.row - 1, self.col), (self.row - 1, self.col + 1), (self.row - 1, self.col + 2), (self.row, self.col - 2),
                    (self.row, self.col - 1), (self.row, self.col), (self.row, self.col + 1), (self.row, self.col + 2),
                    (self.row + 1, self.col - 1), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2),
                    (self.row + 2, self.col - 1), (self.row + 2, self.col), (self.row + 2, self.col + 1)]
        else:
            return [(self.row - 2, self.col - 1), (self.row - 2, self.col), (self.row - 2, self.col + 1), (self.row - 1, self.col - 2),
                    (self.row - 1, self.col - 1), (self.row - 1, self.col), (self.row - 1, self.col + 1), (self.row, self.col - 2),
                    (self.row, self.col - 1), (self.row, self.col), (self.row, self.col + 1), (self.row, self.col + 2),
                    (self.row + 1, self.col - 2), (self.row + 1, self.col - 1), (self.row + 1, self.col), (self.row + 1, self.col + 1),
                    (self.row + 2, self.col - 1), (self.row + 2, self.col), (self.row + 2, self.col + 1)]

class Archer(Ranged):
    def __init__(self, row, col, country, moves=2, defaultMoves=2, selected=False, name="archer", color=None, damage=40, health=50):
        super().__init__(row, col, country, moves, defaultMoves, selected, name, color, damage, health)

    def draw(self, canvas, data):
        row = self.row
        col = self.col
        self.getColor()
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
            canvas.create_rectangle(cx - 10, cy - 15, cx + 10, cy + 15, fill=self.color, outline="SlateBlue1", width=5)
            canvas.create_text(cx, cy, text=self.health, font="ComicSansMS 10", fill="white")
        else:
            startingX = -23
            startingY = 21
            row //= 2
            cx = startingX + (xWidth * col) + (xWidth // 2)
            cy = startingY + (yHeight * row) + (hexagonHeight // 2)
            canvas.create_rectangle(cx - 10, cy - 15, cx + 10, cy + 15, fill=self.color, outline="SlateBlue1", width=5)
            canvas.create_text(cx, cy, text=self.health, font="ComicSansMS 10", fill="white")
