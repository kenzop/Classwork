def setup():
    global megaman, megaman2, time, megamanX
    size(640, 480)
    megaman = loadImage('megaman.png')
    megaman.resize(40, 40)
    megaman2 = loadImage('megaman2.png')
    megaman2.resize(40, 40)
    time = 0
    megamanX = 50
def keyPressed():
    global megamanX, time
    if keyCode == RIGHT:
        megamanX += 2
        time += 1
    if keyCode == LEFT:
        megamanX -= 2
        time += 1
def draw():
    global time
    background(255)
    if time > 4:
        image(megaman2, megamanX, 50)
    elif time <= 4: 
        image(megaman, megamanX, 50)
    if time > 6:
        time = 0
