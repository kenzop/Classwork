x = 0
def setup():
    size(640, 480)
    noStroke()
def drawClouds():
    global x
    y = height/4
    fill('#F3F1E6')
    ellipse(x, y+25, 75, 25)
    ellipse(x, y-25, 75, 50)
    ellipse(x-25, y, 75, 50)
    ellipse(x+25, y, 75, 50)
def drawMountain():
    fill('#D8D5DB')   
    triangle(25, height, 225, height, 112.5, 100)
    triangle(150, height, 350, height, 280, 209)
    triangle(320, height, 525, height, 412.5, 100)
    triangle(520, height, 750, height, 412.5, 100)
def draw():
    background('#007EA7')
    global x
    if x-30 >= width + 25:
        x = 0
    x += 3
    drawMountain()
    drawClouds()
    fill('#32936F')
    rect(0, height-50, width, 50)
