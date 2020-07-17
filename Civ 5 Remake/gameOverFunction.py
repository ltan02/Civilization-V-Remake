def gameOverMousePressed(event, data):
    if event.x >= 500 and event.x <= 1364 and event.y >= 342 and event.y <= 489:
        if data.currentMode == "Singleplayer":
            resetGame(data)
            data.gameMode = "singleplayer"
        elif data.currentMode == "Multiplayer":
            resetGame(data)
            data.gameMode == "Choose Players"

def gameOverKeyPressed(event, data):
    pass

def gameOverTimerFired(data):
    pass

def gameOverRedrawAll(canvas, data):
    canvas.create_image(data.width//2, data.height//2, image=data.gameOverScreen)
