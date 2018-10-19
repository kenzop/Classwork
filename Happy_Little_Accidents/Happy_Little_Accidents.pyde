x = 0
z = 0
ylocation = 480

def setup():
    size(640, 480)
    noStroke()

def drawMountain():
    b = height
    fill('#D0CEBA')
    triangle(-100, b, 200, b, 60, 200)
    triangle(-20, b, 380, b, 180, 270)
    triangle(200, b, 480, b, 360, 300)
    triangle(400, b, 700, b, 550, 250)
 
def drawSun():
    a = width
    b = height
    fill('#FF9000')
    ellipse(a/2, b, 200, 200)

def drawClouds():
    global x
    global z
    fill('#FFFCF7')
    y = height/2
    #cloud 1
    ellipse(x, y+25, 75, 25) #bottom circle
    ellipse(x, y-25, 75, 50) #top circle
    ellipse(x-25, y, 75, 50) #left circle
    ellipse(x+25, y, 75, 50) # right circle
    #cloud 2
    ellipse(z+30, height-325, 75, 25) #bottom circle
    ellipse(z+30,height-375, 75, 50) #top circle
    ellipse(z-5, height-350, 75, 50) #left circle
    ellipse(z+55, height-350, 75, 50) # right circle
def drawTrees():
    a = -5    #x-location of vertex
    b = 480   #y-location of vertex
    fill('#809848')
    while(a < width): #draws trees
        triangle(a, b, a+20, b, a+10, b-40)
        a += 10

def drawBalloon():
    xlocation = 550
    fill('#A1A499')
    rect(xlocation-1, ylocation-40, 2, 40)
    fill(255, 0, 0)
    ellipse(xlocation, ylocation-40, 20, 25)

def draw():
    global x
    global z
    global ylocation
    background('#8DC8FC')
    if x-30 > (width+65):
        x = 0
    x += 1
    
    if z > (width+65):
        z = 0
    z += 2
    ylocation -= 1

    drawMountain()
    drawSun()
    drawClouds()
    drawTrees()
    drawBalloon()
