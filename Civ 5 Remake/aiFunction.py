from tkinter import *
import random
from civilizationClass import *
import math

def AIPossibleMoves(moves, row, col):
        if moves == 0:
            return []

        if moves == 1:
            if row % 2 == 0:
                return [(row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col),
                        (row, col + 1), (row + 1, col), (row + 1, col + 1)]
            else:
                return [(row - 1, col - 1), (row - 1, col), (row, col - 1), (row, col),
                        (row, col + 1), (row + 1, col - 1), (row + 1, col)]

        if moves == 2:
            if row % 2 == 0:
                return [(row - 2, col - 1), (row - 2, col), (row - 2, col + 1), (row - 1, col - 1),
                        (row - 1, col), (row - 1, col + 1), (row - 1, col + 2), (row, col - 2),
                        (row, col - 1), (row, col), (row, col + 1), (row, col + 2),
                        (row + 1, col - 1), (row + 1, col), (row + 1, col + 1), (row + 1, col + 2),
                        (row + 2, col - 1), (row + 2, col), (row + 2, col + 1)]
            else:
                return [(row - 2, col - 1), (row - 2, col), (row - 2, col + 1), (row - 1, col - 2),
                        (row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 2),
                        (row, col - 1), (row, col), (row, col + 1), (row, col + 2),
                        (row + 1, col - 2), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1),
                        (row + 2, col - 1), (row + 2, col), (row + 2, col + 1)]
        return []

def moveAI(data, ai):
    if ai == "usa":
        for eachUnit in data.usaUnits:
            if eachUnit[0] != "City":
                possibleMoves = AIPossibleMoves(eachUnit[0].moves, eachUnit[0].row, eachUnit[0].col)
                nextMove = random.randint(0, len(possibleMoves)-1)
                move = possibleMoves[nextMove]
                if eachUnit[0] in ["warrior", "swordsman"] and eachUnit[0].moves > 0:
                    otherUnits = data.ukUnits + data.frenchUnits + data.germanUnits
                    possibleAttacks = eachUnit[0].possibleAttacks()
                    for units in otherUnits:
                        if move[0] == units[1][0] and move[1] == units[1][1]:
                            eachUnit[0].attack(units[0], data)
                            units[0].retaliate(eachUnit[0], data)

                if eachUnit[0] == "archer" and eachUnit[0].moves > 0:
                    otherUnits = data.usaUnits + data.frenchUnits + data.germanUnits
                    possibleAttacks = eachUnit[0].possibleAttacks()
                    for units in otherUnits:
                        if move[0] == units[1][0] and move[1] == units[1][1]:
                            eachUnit[0].attack(units[0], data)
                            units[0].retaliate(eachUnit[0], data)

                while data.board[move[0]][move[1]] in [2, 5, 6]:
                    nextMove = random.randint(0, len(possibleMoves)-1)
                    move = possibleMoves[nextMove]
                eachUnit[0].moves -= abs(eachUnit[0].row - move[0]) + abs(eachUnit[0].col - move[1])
                if eachUnit[0].moves == 0:
                    eachUnit[0].selected = False
                eachUnit[1] = (move[0], move[1])
                eachUnit[0].row = move[0]
                eachUnit[0].col = move[1]
                data.row = move[0]
                data.col = move[1]


    elif ai == "uk":
        for eachUnit in data.ukUnits:
            if eachUnit[0] != "City":
                possibleMoves = AIPossibleMoves(eachUnit[0].moves, eachUnit[0].row, eachUnit[0].col)
                nextMove = random.randint(0, len(possibleMoves)-1)
                move = possibleMoves[nextMove]
                if eachUnit[0] in ["warrior", "swordsman"] and eachUnit[0].moves > 0:
                    otherUnits = data.usaUnits + data.frenchUnits + data.germanUnits
                    possibleAttacks = eachUnit[0].possibleAttacks()
                    for units in otherUnits:
                        if move[0] == units[1][0] and move[1] == units[1][1]:
                            eachUnit[0].attack(units[0], data)
                            units[0].retaliate(eachUnit[0], data)

                if eachUnit[0] == "archer" and eachUnit[0].moves > 0:
                    otherUnits = data.usaUnits + data.frenchUnits + data.germanUnits
                    possibleAttacks = eachUnit[0].possibleAttacks()
                    for units in otherUnits:
                        if move[0] == units[1][0] and move[1] == units[1][1]:
                            eachUnit[0].attack(units[0], data)
                            units[0].retaliate(eachUnit[0], data)

                while data.board[move[0]][move[1]] in [2, 5, 6]:
                    nextMove = random.randint(0, len(possibleMoves)-1)
                    move = possibleMoves[nextMove]
                eachUnit[0].moves -= abs(eachUnit[0].row - move[0]) + abs(eachUnit[0].col - move[1])
                if eachUnit[0].moves == 0:
                    eachUnit[0].selected = False
                eachUnit[1] = (move[0], move[1])
                eachUnit[0].row = move[0]
                eachUnit[0].col = move[1]
                data.row = move[0]
                data.col = move[1]

    elif ai == "french":
        for eachUnit in data.frenchUnits:
            if eachUnit[0] != "City":
                possibleMoves = AIPossibleMoves(eachUnit[0].moves, eachUnit[0].row, eachUnit[0].col)
                nextMove = random.randint(0, len(possibleMoves)-1)
                move = possibleMoves[nextMove]
                if eachUnit[0] in ["warrior", "swordsman"] and eachUnit[0].moves > 0:
                    otherUnits = data.usaUnits + data.ukUnits + data.germanUnits
                    possibleAttacks = eachUnit[0].possibleAttacks()
                    for units in otherUnits:
                        if move[0] == units[1][0] and move[1] == units[1][1]:
                            eachUnit[0].attack(units[0], data)
                            units[0].retaliate(eachUnit[0], data)

                if eachUnit[0] == "archer" and eachUnit[0].moves > 0:
                    otherUnits = data.usaUnits + data.frenchUnits + data.germanUnits
                    possibleAttacks = eachUnit[0].possibleAttacks()
                    for units in otherUnits:
                        if move[0] == units[1][0] and move[1] == units[1][1]:
                            eachUnit[0].attack(units[0], data)
                            units[0].retaliate(eachUnit[0], data)

                while data.board[move[0]][move[1]] in [2, 5, 6]:
                    nextMove = random.randint(0, len(possibleMoves)-1)
                    move = possibleMoves[nextMove]
                eachUnit[0].moves -= abs(eachUnit[0].row - move[0]) + abs(eachUnit[0].col - move[1])
                if eachUnit[0].moves == 0:
                    eachUnit[0].selected = False
                eachUnit[1] = (move[0], move[1])
                eachUnit[0].row = move[0]
                eachUnit[0].col = move[1]
                data.row = move[0]
                data.col = move[1]

    else:
        for eachUnit in data.germanUnits:
            if eachUnit[0] != "City":
                possibleMoves = AIPossibleMoves(eachUnit[0].moves, eachUnit[0].row, eachUnit[0].col)
                nextMove = random.randint(0, len(possibleMoves)-1)
                move = possibleMoves[nextMove]
                if eachUnit[0] in ["warrior", "swordsman"] and eachUnit[0].moves > 0:
                    otherUnits = data.usaUnits + data.frenchUnits + data.ukUnits
                    possibleAttacks = eachUnit[0].possibleAttacks()
                    for units in otherUnits:
                        if move[0] == units[1][0] and move[1] == units[1][1]:
                            eachUnit[0].attack(units[0], data)
                            units[0].retaliate(eachUnit[0], data)

                if eachUnit[0] == "archer" and eachUnit[0].moves > 0:
                    otherUnits = data.usaUnits + data.frenchUnits + data.germanUnits
                    possibleAttacks = eachUnit[0].possibleAttacks()
                    for units in otherUnits:
                        if move[0] == units[1][0] and move[1] == units[1][1]:
                            eachUnit[0].attack(units[0], data)
                            units[0].retaliate(eachUnit[0], data)

                while data.board[move[0]][move[1]] in [2, 5, 6]:
                    nextMove = random.randint(0, len(possibleMoves)-1)
                    move = possibleMoves[nextMove]
                eachUnit[0].moves -= abs(eachUnit[0].row - move[0]) + abs(eachUnit[0].col - move[1])
                if eachUnit[0].moves == 0:
                    eachUnit[0].selected = False
                eachUnit[1] = (move[0], move[1])
                eachUnit[0].row = move[0]
                eachUnit[0].col = move[1]
                data.row = move[0]
                data.col = move[1]

def actionAI(data):
    for ai in data.AI:
        action = random.choice([0, 0, 0, 1, 2, 3, 4, 5, 6])
        if action == 0:
            moveAI(data, ai)
        elif action == 1:
            if ai == "usa":
                for eachUnit in data.usaUnits:
                    if eachUnit[0] == "settler":
                        eachUnit[0].createCity(data)
                        break

            elif ai == "uk":
                for eachUnit in data.ukUnits:
                    if eachUnit[0] == "settler":
                        eachUnit[0].createCity(data)
                        break

            elif ai == "french":
                for eachUnit in data.frenchUnits:
                    if eachUnit[0] == "settler":
                        eachUnit[0].createCity(data)
                        break

            else:
                for eachUnit in data.germanUnits:
                    if eachUnit[0] == "settler":
                        eachUnit[0].createCity(data)
                        break

        elif action == 2:
            if ai == "usa":
                for eachUnit in data.usaUnits:
                    if eachUnit[0] == "City":
                        if data.usaProduction >= 5:
                            eachUnit[0].aicreateWorker(data)
                            data.usaProduction -= 5
                            data.usaProductionPerTurn += 1
                            break

            elif ai == "uk":
                for eachUnit in data.ukUnits:
                    if eachUnit[0] == "City":
                        if data.ukProduction >= 5:
                            eachUnit[0].aicreateWorker(data)
                            data.ukProduction -= 5
                            data.ukProductionPerTurn += 1
                            break

            elif ai == "french":
                for eachUnit in data.frenchUnits:
                    if eachUnit[0] == "City":
                        if data.frenchProduction >= 5:
                            eachUnit[0].aicreateWorker(data)
                            data.frenchProduction -= 5
                            data.frenchProductionPerTurn += 1
                            break

            elif ai == "germany":
                for eachUnit in data.germanUnits:
                    if eachUnit[0] == "City":
                        if data.germanProduction >= 5:
                            eachUnit[0].aicreateWorker(data)
                            data.germanProduction -= 5
                            data.germanProductionPerTurn += 1
                            break

        elif action == 3:
            if ai == "usa":
                for eachUnit in data.usaUnits:
                    if eachUnit[0] == "City":
                        if data.usaProduction >= 15:
                            eachUnit[0].aicreateSettler(data)
                            data.usaProduction -= 15
                            break

            elif ai == "uk":
                for eachUnit in data.ukUnits:
                    if eachUnit[0] == "City":
                        if data.ukProduction >= 15:
                            eachUnit[0].aicreateSettler(data)
                            data.ukProduction -= 15
                            break

            elif ai == "french":
                for eachUnit in data.frenchUnits:
                    if eachUnit[0] == "City":
                        if data.frenchProduction >= 15:
                            eachUnit[0].aicreateSettler(data)
                            data.frenchProduction -= 15
                            break

            elif ai == "germany":
                for eachUnit in data.germanUnits:
                    if eachUnit[0] == "City":
                        if data.germanProduction >= 15:
                            eachUnit[0].aicreateSettler(data)
                            data.germanProduction -= 15
                            break

        elif action == 4:
            if ai == "usa":
                for eachUnit in data.usaUnits:
                    if eachUnit[0] == "City":
                        if data.usaProduction >= 5:
                            eachUnit[0].aicreateArcher(data)
                            data.usaProduction -= 5
                            break

            elif ai == "uk":
                for eachUnit in data.ukUnits:
                    if eachUnit[0] == "City":
                        if data.ukProduction >= 5:
                            eachUnit[0].aicreateArcher(data)
                            data.ukProduction -= 5
                            break

            elif ai == "french":
                for eachUnit in data.frenchUnits:
                    if eachUnit[0] == "City":
                        if data.frenchProduction >= 5:
                            eachUnit[0].aicreateArcher(data)
                            data.frenchProduction -= 5
                            break

            elif ai == "germany":
                for eachUnit in data.germanUnits:
                    if eachUnit[0] == "City":
                        if data.germanProduction >= 5:
                            eachUnit[0].aicreateArcher(data)
                            data.germanProduction -= 5
                            break

        elif action == 5:
            if ai == "usa":
                for eachUnit in data.usaUnits:
                    if eachUnit[0] == "City":
                        if data.usaProduction >= 10:
                            eachUnit[0].aicreateSwordsman(data)
                            data.usaProduction -= 10
                            break

            elif ai == "uk":
                for eachUnit in data.ukUnits:
                    if eachUnit[0] == "City":
                        if data.ukProduction >= 10:
                            eachUnit[0].aicreateSwordsman(data)
                            data.ukProduction -= 10
                            break

            elif ai == "french":
                for eachUnit in data.frenchUnits:
                    if eachUnit[0] == "City":
                        if data.frenchProduction >= 10:
                            eachUnit[0].aicreateSwordsman(data)
                            data.frenchProduction -= 10
                            break

            elif ai == "germany":
                for eachUnit in data.germanUnits:
                    if eachUnit[0] == "City":
                        if data.germanProduction >= 10:
                            eachUnit[0].aicreateSwordsman(data)
                            data.germanProduction -= 10
                            break

        elif action == 6:
            if ai == "usa":
                for eachUnit in data.usaUnits:
                    if eachUnit[0] == "City":
                        if data.usaProduction >= 7:
                            data.usaProduction -= 7
                            eachUnit[0].aicreateWarrior(data)
                            break

            elif ai == "uk":
                for eachUnit in data.ukUnits:
                    if eachUnit[0] == "City":
                        if data.ukProduction >= 7:
                            eachUnit[0].aicreateWarrior(data)
                            data.ukProduction -= 7
                            break

            elif ai == "french":
                for eachUnit in data.frenchUnits:
                    if eachUnit[0] == "City":
                        if data.frenchProduction >= 7:
                            eachUnit[0].aicreateWarrior(data)
                            data.frenchProduction -= 7
                            break

            elif ai == "germany":
                for eachUnit in data.germanUnits:
                    if eachUnit[0] == "City":
                        if data.germanProduction >= 7:
                            eachUnit[0].aicreateWarrior(data)
                            data.germanProduction -= 7
                            break
