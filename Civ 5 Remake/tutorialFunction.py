from tkinter import *

################################################################
# Tutorial Function
################################################################


def tutorialMousePressed(event, data):
    if data.tutorialPageNumber < 6:
        if nextButtonClicked(event, data):
            data.tutorialPageNumber += 1

    if data.tutorialPageNumber > 1:
        if backButtonClicked(event, data):
            data.tutorialPageNumber -= 1

    if backToHomeScreenClicked(event, data):
        data.gameMode = "Home_Screen"


def nextButtonClicked(event, data):
    return event.x >= data.width - 200 and event.x <= data.width - 50 and event.y >= data.height - 75 and event.y <= data.height - 25


def backButtonClicked(event, data):
    return event.x >= 50 and event.x <= 200 and event.y >= data.height - 75 and event.y <= data.height - 25


def backToHomeScreenClicked(event, data):
    return event.x >= 10 and event.x <= 160 and event.y >= 20 and event.y <= 70


def tutorialKeyPressed(event, data):
    if data.tutorialPageNumber > 1:
        if event.keysym == "Left":
            data.tutorialPageNumber -= 1

    if data.tutorialPageNumber < 2:
        if event.keysym == "Right":
            data.tutorialPageNumber += 1

    if event.keysym == "Escape":
        data.gameMode = "Home_Screen"


def tutorialTimerFired(data):
    pass


def drawBackArrow(canvas, data):
    canvas.create_polygon(50, data.height - 50, 100, data.height - 75, 200, data.height - 75, 200, data.height - 25,
                          100, data.height - 25, fill="white")
    canvas.create_text(150, data.height - 50, text="Back", font="ComicSansMS 25", fill="black")


def drawNextArrow(canvas, data):
    canvas.create_polygon(data.width - 50, data.height - 50, data.width - 100, data.height - 75,
                          data.width - 200, data.height - 75, data.width - 200, data.height - 25,
                          data.width - 100, data.height - 25, fill="white")
    canvas.create_text(data.width - 150, data.height - 50, text="Next", font="ComicSansMS 25", fill="black")


def drawBottomText(canvas, data):
    canvas.create_rectangle(data.width // 2 - 400, data.height - 75, data.width // 2 + 400, data.height - 25, fill="white")
    canvas.create_text(data.width // 2, data.height - 50, text="You can use the left and right arrow keys to navigate or press the buttons",
                       fill="black", font="ComicSansMS 20")


def drawPageNumber(canvas, data):
    canvas.create_rectangle(data.width // 2 - 50, 115, data.width // 2 + 50, 165, fill="white")
    text = "Page %d" % data.tutorialPageNumber
    canvas.create_text(data.width // 2, 140, text=text, fill="black", font="ComicSansMS 15")


def drawTutorialPage1(canvas, data):
    canvas.create_image(data.width//2, data.height//2, image=data.tutorialPage1)


def drawTutorialPage2(canvas, data):
    canvas.create_image(data.width//2, data.height//2, image=data.tutorialPage2)

def tutorialRedrawAll(canvas, data):
    if data.tutorialPageNumber == 1:
        drawTutorialPage1(canvas, data)
    elif data.tutorialPageNumber == 2:
        drawTutorialPage2(canvas, data)

    drawPageNumber(canvas, data)
    if data.tutorialPageNumber > 1:
        drawBackArrow(canvas, data)
    if data.tutorialPageNumber < 2:
        drawNextArrow(canvas, data)

    drawBottomText(canvas, data)

    canvas.create_rectangle(10, 20, 160, 70, fill="black")
    canvas.create_text(85, 45, text="Back to Home Screen", fill="white", font="ComicSansMS 15")
