from tkinter import *
import random
from civilizationClass import *
import math

################################################################
# Helper Function for UI
################################################################


def drawBoard(canvas, data):
    for rows in range(len(data.boardPixel)):
        for cols in range(len(data.boardPixel[rows])):
            cx = data.boardPixel[rows][cols][0]
            cy = data.boardPixel[rows][cols][1]
            elements = data.board[rows][cols]
            if elements == 1:
                #color = "SpringGreen4"
                canvas.create_image(cx, cy, image=data.forestTileGame)
            elif elements == 2:
                #color = "gray64"
                canvas.create_image(cx, cy, image=data.mountainTileGame)
            elif elements == 3:
                #color = "SpringGreen2"
                canvas.create_image(cx, cy, image=data.grassTileGame)
            elif elements == 4:
                color = "khaki1"
                canvas.create_image(cx, cy, image=data.desertTileGame)
            elif elements == 5:
                #color = "cyan2"
                canvas.create_image(cx, cy, image=data.coastTileGame)
            else:
                # color = "blue4"
                canvas.create_image(cx, cy, image=data.seaTileGame)
           # canvas.create_polygon(cx, cy - 27, cx + 23, cy - 12, cx + 23, cy + 20, cx, cy + 35, cx - 23, cy + 20, cx - 23, cy - 12, fill=color, outline="black", width=1.5)


def drawUnits(canvas, data):
    if not(data.gameStarted):
        for eachPlayer in data.players:
            if eachPlayer == "usa":
                for eachUnit in data.usaUnits:
                    eachUnit[0].getColor()
                    eachUnit[0].draw(canvas, data)
            elif eachPlayer == "uk":
                for eachUnit in data.ukUnits:
                    eachUnit[0].getColor()
                    eachUnit[0].draw(canvas, data)
            elif eachPlayer == "french":
                for eachUnit in data.frenchUnits:
                    eachUnit[0].getColor()
                    eachUnit[0].draw(canvas, data)
            else:
                for eachUnit in data.germanUnits:
                    eachUnit[0].getColor()
                    eachUnit[0].draw(canvas, data)


def drawCity(canvas, data):
    for player in data.players:
        if player == "usa":
            for eachUnit in data.usaUnits:
                if eachUnit[0] == "settler" or isinstance(eachUnit[0], City):
                    eachUnit[0].drawCity(canvas, data)
                if isinstance(eachUnit[0], City):
                    eachUnit[0].getCountry(data)
                    eachUnit[0].draw(canvas, data)
        elif player == "uk":
            for eachUnit in data.ukUnits:
                if eachUnit[0] == "settler" or isinstance(eachUnit[0], City):
                    eachUnit[0].drawCity(canvas, data)
                if isinstance(eachUnit[0], City):
                    eachUnit[0].getCountry(data)
                    eachUnit[0].draw(canvas, data)
        elif player == "french":
            for eachUnit in data.frenchUnits:
                if eachUnit[0] == "settler" or isinstance(eachUnit[0], City):
                    eachUnit[0].drawCity(canvas, data)
                if isinstance(eachUnit[0], City):
                    eachUnit[0].getCountry(data)
                    eachUnit[0].draw(canvas, data)
        else:
            for eachUnit in data.germanUnits:
                if eachUnit[0] == "settler" or isinstance(eachUnit[0], City):
                    eachUnit[0].drawCity(canvas, data)
                if isinstance(eachUnit[0], City):
                    eachUnit[0].getCountry(data)
                    eachUnit[0].draw(canvas, data)


def drawMoveTiles(canvas, data):
    player = data.players[data.currentPlayer]
    if player == "usa":
        for eachUnit in data.usaUnits:
            if eachUnit[0].selected == True:
                eachUnit[0].drawMoveTiles(canvas, data, eachUnit[0].row, eachUnit[0].col)
    elif player == "uk":
        for eachUnit in data.ukUnits:
            if eachUnit[0].selected == True:
                eachUnit[0].drawMoveTiles(canvas, data, eachUnit[0].row, eachUnit[0].col)
    elif player == "french":
        for eachUnit in data.frenchUnits:
            if eachUnit[0].selected == True:
                eachUnit[0].drawMoveTiles(canvas, data, eachUnit[0].row, eachUnit[0].col)
    else:
        for eachUnit in data.germanUnits:
            if eachUnit[0].selected == True:
                eachUnit[0].drawMoveTiles(canvas, data, eachUnit[0].row, eachUnit[0].col)


def getRowAndCol(data):
    row = random.randint(0, len(data.board) - 1)
    col = random.randint(0, len(data.board[0]) - 1)
    while data.board[row][col] == 2 or data.board[row][col] == 5 or data.board[row][col] == 6:
        row = random.randint(0, len(data.board) - 1)
        col = random.randint(0, len(data.board[0]) - 1)
    return (row, col)


def drawTopMenu(canvas, data):
    canvas.create_rectangle(0, 0, data.width, 30, fill="black")
    canvas.create_text(30, 15, text="MENU", font="ComicSansMS 12", fill="white")
    canvas.create_text(data.width - 100, 15, text=("Turn: %d" % data.turn), font="ComicSansMS 12", fill="white")

    if data.year < 0:
        yearText = "%d BC" % abs(data.year)
    else:
        yearText = "%d AD" % abs(data.year)

    canvas.create_text(data.width - 40, 15, text=yearText, font="ComicSansMS 12", fill="white")

    if data.players[data.currentPlayer] == "usa":
        color = "red"
        production = data.usaProduction
        productionPerTurn = data.usaProductionPerTurn
    elif data.players[data.currentPlayer] == "uk":
        color = "orange"
        production = data.ukProduction
        productionPerTurn = data.ukProductionPerTurn
    elif data.players[data.currentPlayer] == "french":
        color = "DarkOliveGreen3"
        production = data.frenchProduction
        productionPerTurn = data.frenchProductionPerTurn
    else:
        color = "black"
        production = data.germanProduction
        productionPerTurn = data.germanProductionPerTurn

    canvas.create_rectangle(80, 5, 100, 25, fill=color, outline="white", width=3)

    productionText = "Production: %d (+%d)" % (production, productionPerTurn)

    canvas.create_text(175, 15, text=productionText, font="ComicSansMS 12", fill="white")

    damageText = "Damage: %d" % data.damage
    unitText = "Current Unit is %s" % data.currUnit
    canvas.create_text(300, 15, text=damageText, font="ComicSansMS 12", fill="white")
    canvas.create_text(450, 15, text=unitText, font="ComicSansMS 12", fill="white")



def noUnits(data, player, newRow, newCol):
    allUnits = data.ukUnits + data.usaUnits + data.frenchUnits + data.germanUnits
    if player == "usa":
        for unit in allUnits:
            row, col = unit[1][0], unit[1][1]
            if newRow == row and newCol == col:
                return False
        return True
    elif player == "uk":
        for unit in allUnits:
            row, col = unit[1][0], unit[1][1]
            if newRow == row and newCol == col:
                return False
        return True
    elif player == "french":
        for unit in allUnits:
            row, col = unit[1][0], unit[1][1]
            if newRow == row and newCol == col:
                return False
        return True
    else:
        for unit in allUnits:
            row, col = unit[1][0], unit[1][1]
            if newRow == row and newCol == col:
                return False
        return True


def getDistance(x0, y0, x1, y1):
    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

def checkGameOver(data):
    counter = 0
    for player in data.players:
        if player == "usa":
            if data.usaUnits == [] and data.usaSpawnedCities == []:
                counter += 1
        elif player == "uk":
            if data.ukUnits == [] and data.ukSpawnedCities == []:
                counter += 1
        elif player == "french":
            if data.frenchUnits == [] and data.frenchSpawnedCities == []:
                counter += 1
        else:
            if data.germanUnits == [] and data.germanSpawnedCities == []:
                counter += 1

    if counter == len(data.players)-1:
        return True
    return False



################################################################
# Multiplayer Function
################################################################


def multiPlayerMousePressed(event, data):
    player = data.players[data.currentPlayer]
    for rows in range(len(data.boardPixel)):
        for cols in range(len(data.boardPixel[rows])):
            if((getDistance(data.boardPixel[rows][cols][0], data.boardPixel[rows][cols][1], event.x, event.y) < data.xWidth // 2) and
                    (getDistance(data.boardPixel[rows][cols][0], data.boardPixel[rows][cols][1], event.x, event.y) < data.yHeight // 2)):
                row = rows
                col = cols

    if player == "usa":
        for units in range(len(data.usaUnits)):
            eachUnit = data.usaUnits[units]
            if eachUnit[0] != "City" and eachUnit[0].clicked(data, row, col) and eachUnit[0].moves > 0:
                if eachUnit[0].selected == False:
                    data.row, data.col = row, col
                    eachUnit[0].selected = True
                    data.currUnit = eachUnit[0]
                    data.damage = eachUnit[0].damage
                else:
                    eachUnit[0].selected = False
            elif eachUnit[0] == "City":
                if eachUnit[0].selected == False:
                    eachUnit[0].selected = True
                    data.currUnit = eachUnit[0]
                    data.damage = eachUnit[0].damage
                else:
                    eachUnit[0].selected = False

            if eachUnit[0] in ["warrior", "swordsman"] and eachUnit[0].selected and eachUnit[0].moves > 0:
                otherUnits = data.usaUnits + data.frenchUnits + data.germanUnits
                possibleAttacks = eachUnit[0].possibleAttacks()
                for units in otherUnits:
                    if row == units[1][0] and col == units[1][1]:
                        eachUnit[0].attack(units[0], data)
                        units[0].retaliate(eachUnit[0], data)

            if eachUnit[0] == "archer" and eachUnit[0].selected and eachUnit[0].moves > 0:
                otherUnits = data.usaUnits + data.frenchUnits + data.germanUnits
                possibleAttacks = eachUnit[0].possibleAttacks()
                for units in otherUnits:
                    if row == units[1][0] and col == units[1][1]:
                        eachUnit[0].attack(units[0], data)
                        units[0].retaliate(eachUnit[0], data)

            if eachUnit[0] != "City" and eachUnit[0].selected and eachUnit[0].moves > 0:
                tmpRow, tmpCol = data.row, data.col
                cityTiles = eachUnit[0].possibleMoves()
                for eachTile in cityTiles:
                    if(eachTile[0] == row and eachTile[1] == col and data.board[eachTile[0]][eachTile[1]] not in [2, 5, 6] and
                        noUnits(data, player, eachTile[0], eachTile[1])):
                        eachUnit[0].moves -= abs(eachUnit[0].row - row) + abs(eachUnit[0].col - col)
                        if eachUnit[0].moves == 0:
                            eachUnit[0].selected = False
                        eachUnit[1] = (row, col)
                        eachUnit[0].row = row
                        eachUnit[0].col = col
                        data.row = row
                        data.col = col

    elif player == "uk":
        for eachUnit in data.ukUnits:
            if eachUnit[0] != "City" and eachUnit[0].clicked(data, row, col) and eachUnit[0].moves > 0:
                if eachUnit[0].selected == False:
                    data.row, data.col = row, col
                    eachUnit[0].selected = True
                    data.currUnit = eachUnit[0]
                    data.damage = eachUnit[0].damage
                else:
                    eachUnit[0].selected = False
            elif eachUnit[0] == "City":
                if eachUnit[0].selected == False:
                    eachUnit[0].selected = True
                    data.currUnit = eachUnit[0]
                    data.damage = eachUnit[0].damage
                else:
                    eachUnit[0].selected = False

            if eachUnit[0] in ["warrior", "swordsman"] and eachUnit[0].selected and eachUnit[0].moves > 0:
                otherUnits = data.usaUnits + data.frenchUnits + data.germanUnits
                possibleAttacks = eachUnit[0].possibleAttacks()
                for units in otherUnits:
                    if row == units[1][0] and col == units[1][1]:
                        eachUnit[0].attack(units[0], data)
                        units[0].retaliate(eachUnit[0], data)

            if eachUnit[0] == "archer" and eachUnit[0].selected and eachUnit[0].moves > 0:
                otherUnits = data.usaUnits + data.frenchUnits + data.germanUnits
                possibleAttacks = eachUnit[0].possibleAttacks()
                for units in otherUnits:
                    if row == units[1][0] and col == units[1][1]:
                        eachUnit[0].attack(units[0], data)
                        units[0].retaliate(eachUnit[0], data)

            if eachUnit[0] != "City" and eachUnit[0].selected and eachUnit[0].moves > 0:
                tmpRow, tmpCol = data.row, data.col
                cityTiles = eachUnit[0].possibleMoves()
                for eachTile in cityTiles:
                    if(eachTile[0] == row and eachTile[1] == col and data.board[eachTile[0]][eachTile[1]] not in [2, 5, 6] and
                        noUnits(data, player, eachTile[0], eachTile[1])):
                        eachUnit[0].moves -= abs(eachUnit[0].row - row) + abs(eachUnit[0].col - col)
                        if eachUnit[0].moves == 0:
                            eachUnit[0].selected = False
                        eachUnit[1] = (row, col)
                        eachUnit[0].row = row
                        eachUnit[0].col = col
                        data.row = row
                        data.col = col

    elif player == "french":
        for eachUnit in data.frenchUnits:
            if eachUnit[0] != "City" and eachUnit[0].clicked(data, row, col) and eachUnit[0].moves > 0:
                if eachUnit[0].selected == False:
                    data.row, data.col = row, col
                    eachUnit[0].selected = True
                    data.currUnit = eachUnit[0]
                    data.damage = eachUnit[0].damage
                else:
                    eachUnit[0].selected = False
            elif eachUnit[0] == "City":
                if eachUnit[0].selected == False:
                    eachUnit[0].selected = True
                    data.currUnit = eachUnit[0]
                    data.damage = eachUnit[0].damage
                else:
                    eachUnit[0].selected = False

            if eachUnit[0] in ["warrior", "swordsman"] and eachUnit[0].selected and eachUnit[0].moves > 0:
                otherUnits = data.usaUnits + data.frenchUnits + data.germanUnits
                possibleAttacks = eachUnit[0].possibleAttacks()
                for units in otherUnits:
                    if row == units[1][0] and col == units[1][1]:
                        eachUnit[0].attack(units[0], data)
                        units[0].retaliate(eachUnit[0], data)

            if eachUnit[0] == "archer" and eachUnit[0].selected and eachUnit[0].moves > 0:
                otherUnits = data.usaUnits + data.frenchUnits + data.germanUnits
                possibleAttacks = eachUnit[0].possibleAttacks()
                for units in otherUnits:
                    if row == units[1][0] and col == units[1][1]:
                        eachUnit[0].attack(units[0], data)
                        units[0].retaliate(eachUnit[0], data)

            if eachUnit[0] != "City" and eachUnit[0].selected and eachUnit[0].moves > 0:
                tmpRow, tmpCol = data.row, data.col
                cityTiles = eachUnit[0].possibleMoves()
                for eachTile in cityTiles:
                    if(eachTile[0] == row and eachTile[1] == col and data.board[eachTile[0]][eachTile[1]] not in [2, 5, 6] and
                        noUnits(data, player, eachTile[0], eachTile[1])):
                        eachUnit[0].moves -= abs(eachUnit[0].row - row) + abs(eachUnit[0].col - col)
                        if eachUnit[0].moves == 0:
                            eachUnit[0].selected = False
                        eachUnit[1] = (row, col)
                        eachUnit[0].row = row
                        eachUnit[0].col = col
                        data.row = row
                        data.col = col
    else:
        for eachUnit in data.germanUnits:
            if eachUnit[0] != "City" and eachUnit[0].clicked(data, row, col) and eachUnit[0].moves > 0:
                if eachUnit[0].selected == False:
                    data.row, data.col = row, col
                    eachUnit[0].selected = True
                    data.currUnit = eachUnit[0]
                    data.damage = eachUnit[0].damage
                else:
                    eachUnit[0].selected = False
            elif eachUnit[0] == "City":
                if eachUnit[0].selected == False:
                    eachUnit[0].selected = True
                    data.currUnit = eachUnit[0]
                    data.damage = eachUnit[0].damage
                else:
                    eachUnit[0].selected = False

            if eachUnit[0] in ["warrior", "swordsman"] and eachUnit[0].selected and eachUnit[0].moves > 0:
                otherUnits = data.usaUnits + data.frenchUnits + data.germanUnits
                possibleAttacks = eachUnit[0].possibleAttacks()
                for units in otherUnits:
                    if row == units[1][0] and col == units[1][1]:
                        eachUnit[0].attack(units[0], data)
                        units[0].retaliate(eachUnit[0], data)

            if eachUnit[0] == "archer" and eachUnit[0].selected and eachUnit[0].moves > 0:
                otherUnits = data.usaUnits + data.frenchUnits + data.germanUnits
                possibleAttacks = eachUnit[0].possibleAttacks()
                for units in otherUnits:
                    if row == units[1][0] and col == units[1][1]:
                        eachUnit[0].attack(units[0], data)
                        units[0].retaliate(eachUnit[0], data)

            if eachUnit[0] != "City" and eachUnit[0].selected and eachUnit[0].moves > 0:
                tmpRow, tmpCol = data.row, data.col
                cityTiles = eachUnit[0].possibleMoves()
                for eachTile in cityTiles:
                    if(eachTile[0] == row and eachTile[1] == col and data.board[eachTile[0]][eachTile[1]] not in [2, 5, 6] and
                        noUnits(data, player, eachTile[0], eachTile[1])):
                        eachUnit[0].moves -= abs(eachUnit[0].row - row) + abs(eachUnit[0].col - col)
                        if eachUnit[0].moves == 0:
                            eachUnit[0].selected = False
                        eachUnit[1] = (row, col)
                        eachUnit[0].row = row
                        eachUnit[0].col = col
                        data.row = row
                        data.col = col


def multiPlayerKeyPressed(event, data):
    if event.keysym == "Escape":  # Make an escape menu
        data.gameMode = "Home_Screen"
    if event.keysym == "space":
        player = data.players[data.currentPlayer]
        if player == "usa":
            for eachUnit in data.usaUnits:
                if eachUnit[0] == "settler" and eachUnit[0].selected:
                    eachUnit[0].createCity(data)
                    break
        elif player == "uk":
            for eachUnit in data.ukUnits:
                if eachUnit[0] == "settler" and eachUnit[0].selected:
                    eachUnit[0].createCity(data)
                    break

        elif player == "french":
            for eachUnit in data.frenchUnits:
                if eachUnit[0] == "settler" and eachUnit[0].selected:
                    eachUnit[0].createCity(data)
                    break
        else:
            for eachUnit in data.germanUnits:
                if eachUnit[0] == "settler" and eachUnit[0].selected:
                    eachUnit[0].createCity(data)
                    break

    if event.char == "w":
        player = data.players[data.currentPlayer]
        if player == "usa":
            for eachUnit in data.usaUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.usaProduction >= 5:
                        eachUnit[0].createWorker(data)
                        data.usaProduction -= 5
                        data.usaProductionPerTurn += 1
                        break

        elif player == "uk":
            for eachUnit in data.ukUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.ukProduction >= 5:
                        eachUnit[0].createWorker(data)
                        data.ukProduction -= 5
                        data.ukProductionPerTurn += 1
                        break

        elif player == "french":
            for eachUnit in data.frenchUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.frenchProduction >= 5:
                        eachUnit[0].createWorker(data)
                        data.frenchProduction -= 5
                        data.frenchProductionPerTurn += 1
                        break

        elif player == "germany":
            for eachUnit in data.germanUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.germanProduction >= 5:
                        eachUnit[0].createWorker(data)
                        data.germanProduction -= 5
                        data.germanProductionPerTurn += 1
                        break

    if event.char == "q":
        player = data.players[data.currentPlayer]
        if player == "usa":
            for eachUnit in data.usaUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.usaProduction >= 7:
                        data.usaProduction -= 7
                        eachUnit[0].createWarrior(data)
                        break
        elif player == "uk":
            for eachUnit in data.ukUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.ukProduction >= 7:
                        eachUnit[0].createWarrior(data)
                        data.ukProduction -= 7
                        break

        elif player == "french":
            for eachUnit in data.frenchUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.frenchProduction >= 7:
                        eachUnit[0].createWarrior(data)
                        data.frenchProduction -= 7
                        break

        elif player == "germany":
            for eachUnit in data.germanUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.germanProduction >= 7:
                        eachUnit[0].createWarrior(data)
                        data.germanProduction -= 7
                        break

    if event.char == "e":
        player = data.players[data.currentPlayer]
        if player == "usa":
            for eachUnit in data.usaUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.usaProduction >= 10:
                        eachUnit[0].createSwordsman(data)
                        data.usaProduction -= 10
                        break

        elif player == "uk":
            for eachUnit in data.ukUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.ukProduction >= 10:
                        eachUnit[0].createSwordsman(data)
                        data.ukProduction -= 10
                        break

        elif player == "french":
            for eachUnit in data.frenchUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.frenchProduction >= 10:
                        eachUnit[0].createSwordsman(data)
                        data.frenchProduction -= 10
                        break

        elif player == "germany":
            for eachUnit in data.germanUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.germanProduction >= 10:
                        eachUnit[0].createSwordsman(data)
                        data.germanProduction -= 10
                        break

    if event.char == "r":
        player = data.players[data.currentPlayer]
        if player == "usa":
            for eachUnit in data.usaUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.usaProduction >= 5:
                        eachUnit[0].createArcher(data)
                        data.usaProduction -= 5
                        break

        elif player == "uk":
            for eachUnit in data.ukUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.ukProduction >= 5:
                        eachUnit[0].createArcher(data)
                        data.ukProduction -= 5
                        break

        elif player == "french":
            for eachUnit in data.frenchUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.frenchProduction >= 5:
                        eachUnit[0].createArcher(data)
                        data.frenchProduction -= 5
                        break

        elif player == "germany":
            for eachUnit in data.germanUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.germanProduction >= 5:
                        eachUnit[0].createArcher(data)
                        data.germanProduction -= 5
                        break

    if event.char == "t":
        player = data.players[data.currentPlayer]
        if player == "usa":
            for eachUnit in data.usaUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.usaProduction >= 15:
                        eachUnit[0].createSettler(data)
                        data.usaProduction -= 15
                        break

        elif player == "uk":
            for eachUnit in data.ukUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.ukProduction >= 15:
                        eachUnit[0].createSettler(data)
                        data.ukProduction -= 15
                        break

        elif player == "french":
            for eachUnit in data.frenchUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.frenchProduction >= 15:
                        eachUnit[0].createSettler(data)
                        data.frenchProduction -= 15
                        break

        elif player == "germany":
            for eachUnit in data.germanUnits:
                if eachUnit[0] == "City" and eachUnit[0].selected:
                    if data.germanProduction >= 15:
                        eachUnit[0].createSettler(data)
                        data.germanProduction -= 15
                        break

    if event.keysym == "Return":
        data.currentPlayer += 1
        if data.currentPlayer == len(data.players):
            data.turn += 1
            data.year += 100
            data.currentPlayer = 0
            for player in data.players:
                if player == "usa":
                    data.usaProduction += data.usaProductionPerTurn
                    for eachUnit in data.usaUnits:
                        eachUnit[0].selected = False
                        if eachUnit[0] != "City":
                            eachUnit[0].moves = eachUnit[0].defaultMoves

                elif player == "uk":
                    data.ukProduction += data.ukProductionPerTurn
                    for eachUnit in data.ukUnits:
                        eachUnit[0].selected = False
                        if eachUnit[0] != "City":
                            eachUnit[0].moves = eachUnit[0].defaultMoves

                elif player == "french":
                    data.frenchProduction += data.frenchProductionPerTurn
                    for eachUnit in data.frenchUnits:
                        eachUnit[0].selected = False
                        if eachUnit[0] != "City":
                            eachUnit[0].moves = eachUnit[0].defaultMoves

                else:
                    data.germanProduction += data.germanProductionPerTurn
                    for eachUnit in data.germanUnits:
                        eachUnit[0].selected = False
                        if eachUnit[0] != "City":
                            eachUnit[0].moves = eachUnit[0].defaultMoves


def multiPlayerTimerFired(data):
    if data.gameStarted:
        for eachPlayer in data.players:
            row, col = getRowAndCol(data)
            if eachPlayer == "usa":
                data.usaUnits.append([Settler(row, col, "usa"), (row, col)])
            elif eachPlayer == "uk":
                data.ukUnits.append([Settler(row, col, "uk"), (row, col)])
            elif eachPlayer == "french":
                data.frenchUnits.append([Settler(row, col, "french"), (row, col)])
            else:
                data.germanUnits.append([Settler(row, col, "german"), (row, col)])
        data.gameStarted = False

    if checkGameOver(data):
        data.currentMode = "Multiplayer"
        data.gameMode = "Game Over"


def multiPlayerRedrawAll(canvas, data):
    drawBoard(canvas, data)
    drawMoveTiles(canvas, data)
    drawUnits(canvas, data)
    drawCity(canvas, data)
    drawTopMenu(canvas, data)
