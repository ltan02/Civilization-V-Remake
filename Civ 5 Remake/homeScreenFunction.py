from tkinter import *

################################################################
# Home Screen Function
################################################################


def homeScreenMousePressed(event, data):
    buttonClicked(event, data, data.distanceBetweenButtons)


def homeScreenKeyPressed(event, data):
    pass


def homeScreenTimerFired(data):
    pass


def drawButtons(canvas, data, x0, y0, x1, y1):
    distanceBetweenButtons = (y1 - y0) // 3
    startingY = y0

    for eachLine in range(2):
        y0 += distanceBetweenButtons
        y1 = y0
        canvas.create_line(x0, y0, x1, y1, fill="white", width=5)

    cy = startingY + (distanceBetweenButtons // 2)
    cx = data.width // 2
    for eachText in ["Single Player", "Multiplayer", "Tutorial"]:
        canvas.create_text(cx, cy, text=eachText, fill="white", font="ComicSansMS 40")
        cy += distanceBetweenButtons

    return distanceBetweenButtons


def buttonClicked(event, data, distanceBetweenButtons):
    cx = data.width // 2
    cy1 = ((data.height // 10) + 120) + (distanceBetweenButtons // 2)
    cy2 = cy1 + distanceBetweenButtons
    cy3 = cy2 + distanceBetweenButtons
    dx, dy = 200, distanceBetweenButtons // 2
    if event.x >= cx - dx and event.x <= cx + dx and event.y >= cy1 - dy and event.y <= cy1 + dy:
        data.gameMode = "Single Player"
        data.gameStarted = True
    elif event.x >= cx - dx and event.x <= cx + dx and event.y >= cy2 - dy and event.y <= cy2 + dy:
        data.gameMode = "Choose Players"
    elif event.x >= cx - dx and event.x <= cx + dx and event.y >= cy3 - dy and event.y <= cy3 + dy:
        data.gameMode = "Tutorial"


def homeScreenRedrawAll(canvas, data):
    canvas.create_image(0, 0, anchor=NW, image=data.homeScreenBackground)
    height = data.height // 10
    canvas.create_text(data.width // 2, height, text=data.name1, font="ComicSansMS 100", fill="DarkGoldenrod1")
    canvas.create_text(data.width // 2, height + 70, text=data.name2, font="ComicSansMS 20", fill="DarkGoldenrod1")
    x0, y0 = (data.width // 2) - 200, height + 120
    x1, y1 = (data.width // 2) + 200, y0 + 600
    canvas.create_rectangle(x0, y0, x1, y1, fill="black")
    data.distanceBetweenButtons = drawButtons(canvas, data, x0, y0, x1, y1)
