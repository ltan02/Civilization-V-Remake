#Citations:
#Run() function taken from course website
#Desert Tile image taken from https://www.masterfile.com/search/en/sahara+desert+birds+eye+view
#Coast Tile image taken from https://www.shutterstock.com/video/clip-2624456-stock-footage-ripples-and-waves-on-blue-sea-surface.html
#Ocean Tile image taken from https://stock-clip.com/video-footage/top+shot+sea/4
#Forest Tile image taken from https://www.pond5.com/stock-footage/12676929/wing-field-and-forest-bird-eye-2.html
#Grass Tile image taken from https://giphy.com/gifs/grass-B4NtO0wsSTpmw
#Mountain Tile image taken from http://www.kartenportal.ch/en/maps/birds-eye-map/
#Home Screen Background taken from http://steamtradingcards.wikia.com/wiki/File:Civilization_V_Background_Wonders.jpg
#Tutorial Screen Background taken from https://arstechnica.com/gaming/2016/09/civilization-civ-6-preview-hands-on/

from tkinter import *
from math import cos, sin, sqrt, radians
import string
import random

################################################################
# Seperate Files
################################################################

#Tutorial Page
from tutorialFunction import *

#Home Screen Page
from homeScreenFunction import *

#Single Player Page
from singlePlayerFunction import *

#Multiplayer Page
from multiPlayerFunction import *

#Civilization Classes
from civilizationClass import *

################################################################
# Main Function
################################################################

def createBoard():
    return [[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
            [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
            [6,6,5,5,5,5,5,5,5,6,5,6,5,5,6,5,5,1,3,3,3,1,5,5,5,5,5,5,5,5,6,6,6],
            [6,6,6,5,1,3,3,3,1,5,5,5,5,5,5,5,5,3,1,4,3,1,1,1,3,3,3,3,3,5,6,6,6,6],
            [6,6,6,5,1,1,1,1,3,3,3,3,3,3,1,1,1,1,1,3,1,1,1,1,3,5,5,5,3,3,5,6,6],
            [6,6,6,5,6,5,5,3,3,1,3,3,3,2,2,1,3,3,3,1,1,3,3,3,5,5,6,5,1,5,5,6,6,6],
            [6,6,6,6,6,5,3,3,3,3,3,1,3,1,3,3,5,3,3,3,4,4,4,5,6,5,5,5,1,5,6,6,6],
            [6,6,6,5,5,3,3,1,5,5,5,3,1,1,4,3,4,4,1,4,4,4,5,5,5,5,3,1,3,5,5,6,6,6],
            [6,6,6,6,5,3,3,3,3,5,5,5,5,1,1,1,1,1,5,5,3,3,5,5,4,5,5,3,3,1,5,6,6],
            [6,6,5,6,6,5,5,5,3,3,1,5,5,5,4,4,4,4,5,5,3,3,3,5,3,3,1,1,3,5,5,6,6,6],
            [6,5,6,6,6,6,6,5,1,1,1,1,3,4,4,4,3,3,5,5,3,1,3,1,1,1,3,5,3,1,5,6,6],
            [6,3,5,6,6,5,6,5,2,1,3,3,1,3,2,5,2,1,3,3,3,3,3,3,1,1,1,5,3,3,5,6,6,6],
            [6,1,5,6,5,6,6,5,1,3,3,2,4,5,5,5,5,5,5,3,5,1,5,5,4,4,5,5,3,3,5,6,6],
            [6,3,3,4,4,4,5,5,5,5,3,3,2,5,5,5,5,5,5,3,1,5,5,5,5,5,5,5,4,4,4,5,6,6],
            [6,3,3,4,4,4,6,5,5,5,3,4,5,5,6,6,6,6,5,5,3,1,1,3,5,5,6,5,4,4,4,5,6],
            [6,3,4,4,1,1,1,1,1,2,3,2,3,5,6,6,6,6,6,5,1,3,3,1,5,6,6,5,4,4,4,5,6,6],
            [6,5,5,4,5,5,5,4,4,4,5,6,5,6,6,6,6,5,5,3,1,1,5,2,5,5,6,5,4,4,4,5,6],
            [6,5,1,4,5,6,6,5,4,4,5,5,5,6,6,6,6,5,3,1,1,3,5,5,5,6,6,5,5,5,5,5,6,6],
            [6,5,5,3,5,5,5,1,3,1,5,6,6,6,6,6,5,5,5,2,2,2,5,6,6,6,6,5,6,6,6,5,6],
            [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
            [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]]

def getImages(data):
    data.forestTileGame = PhotoImage(file="forestTile.gif")
    data.coastTileGame = PhotoImage(file="coastTile.gif")
    data.desertTileGame = PhotoImage(file="desertTile.gif")
    data.grassTileGame = PhotoImage(file="grassTile.gif")
    data.mountainTileGame = PhotoImage(file="mountainTile.gif")
    data.seaTileGame = PhotoImage(file="seaTile.gif")

    data.gameOverScreen = PhotoImage(file="Game_Over_Screen.png")
    data.choosePlayers = PhotoImage(file="ChoosePlayers.png")

    data.tutorialPage1 = PhotoImage(file="TutorialPage1.png")
    data.tutorialPage2 = PhotoImage(file="TutorialPage2.png")

def getPlayerInfo(data):
    players = random.randint(2, 4)
    for eachPlayer in range(players):
        country = random.choice(data.countries)
        data.players.append(country)
        data.countries.remove(country)

def getBoardPixels(data):
    cy = 0
    counter = 0
    for rows in data.board:
        tempRow = []
        if counter % 2 == 0:
            cx = 23
        else:
            cx = 0
        for cols in rows:
            tempRow.append((cx, cy))
            cx += 46
        cy += 46
        counter += 1
        data.boardPixel.append(tempRow)

def resetGame(data):
    data.usaCitiesUnchanged = ["Washington", "New York", "Boston", "Philadelphia", "Atlanta"]
    data.usaCities = ["Washington", "New York", "Boston", "Philadelphia", "Atlanta"]
    data.usaUnits = []
    data.usaTempCity = []
    data.usaSpawnedCities = []
    data.usaProduction = 5
    data.ukProductionPerTurn = 1

    data.ukCitiesUnchanged = ["London", "York", "Nottingham", "Hastings", "Canterbury"]
    data.ukCities = ["London", "York", "Nottingham", "Hastings", "Canterbury"]
    data.ukUnits = []
    data.ukTempCity = []
    data.ukSpawnedCities = []
    data.ukProduction = 5
    data.ukProductionPerTurn = 1

    data.frenchCitiesUnchanged = ["Paris", "Orleans", "Lyon", "Troyes", "Tours"]
    data.frenchCities = ["Paris", "Orleans", "Lyon", "Troyes", "Tours"]
    data.frenchUnits = []
    data.frenchTempCity = []
    data.frenchSpawnedCities = []
    data.frenchProduction = 5
    data.frenchProductionPerTurn = 1

    data.germanCitiesUnchanged = ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt"]
    data.germanCities = ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt"]
    data.germanUnits = []
    data.germanTempCity = []
    data.germanSpawnedCities = []
    data.germanProduction = 5
    data.germanProductionPerTurn = 1

    data.gameChanged = 0
    data.players = []

def init(data):
    data.gameMode = "Home_Screen"
    data.homeScreenBackground = PhotoImage(file="background.png")
    data.name1 = "Civilization V"
    data.name2 = "The Remix"
    data.distanceBetweenButtons = 0
    data.tutorialPageNumber = 1
    data.xWidth = 45
    data.yHeight = 56
    data.board = createBoard()
    getImages(data)
    data.currentMode = "Singleplayer"

    data.boardPixel = []
    getBoardPixels(data)

    data.row = 0
    data.col = 0
    data.currentPlayer = 0
    data.damage = 0
    data.currUnit = ""

    data.settlers = []
    data.turn = 1
    data.year = -2000
    data.gameStarted = False
    data.gameChanged = 0
    data.drawCity = False
    data.outline = "black"
    data.counterRows = 0
    data.counterCols = 0

    data.usaCitiesUnchanged = ["Washington", "New York", "Boston", "Philadelphia", "Atlanta"]
    data.usaCities = ["Washington", "New York", "Boston", "Philadelphia", "Atlanta"]
    data.usaUnits = []
    data.usaTempCity = []
    data.usaSpawnedCities = []
    data.usaProduction = 5
    data.usaProductionPerTurn = 1

    data.ukCitiesUnchanged = ["London", "York", "Nottingham", "Hastings", "Canterbury"]
    data.ukCities = ["London", "York", "Nottingham", "Hastings", "Canterbury"]
    data.ukUnits = []
    data.ukTempCity = []
    data.ukSpawnedCities = []
    data.ukProduction = 5
    data.ukProductionPerTurn = 1

    data.frenchCitiesUnchanged = ["Paris", "Orleans", "Lyon", "Troyes", "Tours"]
    data.frenchCities = ["Paris", "Orleans", "Lyon", "Troyes", "Tours"]
    data.frenchUnits = []
    data.frenchTempCity = []
    data.frenchSpawnedCities = []
    data.frenchProduction = 5
    data.frenchProductionPerTurn = 1

    data.germanCitiesUnchanged = ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt"]
    data.germanCities = ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt"]
    data.germanUnits = []
    data.germanTempCity = []
    data.germanSpawnedCities = []
    data.germanProduction = 5
    data.germanProductionPerTurn = 1

    data.cantBuildUnit = False

    data.countries = ["usa", "uk", "french", "germany"]

    data.players = []

    data.gameOver = False

    data.singlePlayer = random.choice(data.countries)
    data.AI = []

    for country in data.countries:
        if country != data.singlePlayer:
            data.AI.append(country)

    data.allPlayers = [data.singlePlayer] + data.AI


def mousePressed(event, data):
    if data.gameMode == "Home_Screen":
        homeScreenMousePressed(event, data)
    elif data.gameMode == "Tutorial":
        tutorialMousePressed(event, data)
    elif data.gameMode == "Single Player":
        singlePlayerMousePressed(event, data)
    elif data.gameMode == "Multiplayer":
        multiPlayerMousePressed(event, data)
    elif data.gameMode == "Game Over":
        gameOverMousePressed(event, data)
    elif data.gameMode == "Choose Players":
        choosePlayersMousePressed(event, data)


def keyPressed(event, data):
    if data.gameMode == "Home_Screen":
        homeScreenKeyPressed(event, data)
    elif data.gameMode == "Tutorial":
        tutorialKeyPressed(event, data)
    elif data.gameMode == "Single Player":
        singlePlayerKeyPressed(event, data)
    elif data.gameMode == "Multiplayer":
        multiPlayerKeyPressed(event, data)
    elif data.gameMode == "Game Over":
        gameOverKeyPressed(event, data)
    elif data.gameMode == "Choose Players":
        choosePlayersKeyPressed(event, data)


def timerFired(data):
    if data.gameMode == "Home_Screen":
        resetGame(data)
        homeScreenTimerFired(data)
    elif data.gameMode == "Tutorial":
        tutorialTimerFired(data)
    elif data.gameMode == "Single Player":
        singlePlayerTimerFired(data)
    elif data.gameMode == "Multiplayer":
        while data.gameChanged <= 1:
            data.gameStarted = True
            data.gameChanged += 1
        multiPlayerTimerFired(data)
    elif data.gameMode == "Game Over":
        gameOverTimerFired(data)
    elif data.gameMode == "Choose Players":
        choosePlayersTimerFired(data)


def redrawAll(canvas, data):
    if data.gameMode == "Home_Screen":
        homeScreenRedrawAll(canvas, data)
    elif data.gameMode == "Tutorial":
        tutorialRedrawAll(canvas, data)
    elif data.gameMode == "Single Player":
        singlePlayerRedrawAll(canvas, data)
    elif data.gameMode == "Multiplayer":
        multiPlayerRedrawAll(canvas, data)
    elif data.gameMode == "Game Over":
        gameOverRedrawAll(canvas, data)
    elif data.gameMode == "Choose Players":
        choosePlayersRedrawAll(canvas, data)

################################################################
# Game Over Screen
################################################################

def gameOverMousePressed(event, data):
    if event.x >= 500 and event.x <= 1366 and event.y >= 471 and event.y <= 620:
        data.gameMode = "Home_Screen"

def gameOverKeyPressed(event, data):
    pass

def gameOverTimerFired(data):
    pass

def gameOverRedrawAll(canvas, data):
    canvas.create_image(data.width//2, data.height//2, image=data.gameOverScreen)

################################################################
# Choose Players Screen
################################################################

def choosePlayersMousePressed(event, data):
    if event.x >= 411 and event.x <= 1095 and event.y >= 291 and event.y <= 403:
        while len(data.players) != 2:
            tmp = random.choice(data.countries)
            while tmp in data.players:
                tmp = random.choice(data.countries)
            data.players.append(tmp)
        data.gameMode = "Multiplayer"
    elif event.x >= 411 and event.x <= 1095 and event.y >= 478 and event.y <= 593:
        while len(data.players) != 3:
            tmp = random.choice(data.countries)
            while tmp in data.players:
                tmp = random.choice(data.countries)
            data.players.append(tmp)
        data.gameMode = "Multiplayer"
    elif event.x >= 411 and event.x <= 1095 and event.y >= 665 and event.y <= 778:
        for country in data.countries:
            data.players.append(country)
        data.gameMode = "Multiplayer"

def choosePlayersKeyPressed(event, data):
    if event.keysym == "Escape":
        data.gameMode = "Home_Screen"

def choosePlayersTimerFired(data):
    pass

def choosePlayersRedrawAll(canvas, data):
    canvas.create_image(data.width//2, data.height//2, image=data.choosePlayers)

################################################################
# Do not change code below
################################################################


def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed



run(1500, 900)
