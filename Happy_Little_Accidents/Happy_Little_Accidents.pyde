x = 0 # used to track the x position of cloud 1
z = 0 # used to track the x position of cloud 2
ylocation = 480 # used to elevate the balloon

def setup():
    size(640, 480)
    noStroke()
    
def drawMountain():
    b = height #The height of the canvas
    fill('#D0CEBA')
    triangle(-100, b, 200, b, 60, 200)
    triangle(-20, b, 380, b, 180, 270)
    triangle(200, b, 480, b, 360, 300)
    triangle(400, b, 700, b, 550, 250)
 
def drawSun():
    a = 50 #The width of the canvas
    b = 40 #The height of the canvas
    fill('#FFFF00')
    ellipse(a, b, 60, 60)

def drawClouds():
    global x #globalize x so that it can be used to track cloud 1's x location
    global z #globalize z so that it can be used to track cloud 2's x location
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

def drawCabins():
    a = 50 # width of the house
    b = 40 # height of the house
    universal = 0
    while universal < width:
        fill('#CA8F42')
        rect(universal, height-b, a, b)
        rect(universal+35, height-(b+18), 10, 20)
        fill('#B06660')
        triangle(universal, height-b, universal+50, height-b, universal+25, height-(b+20))
        fill('#5594ED')
        rect(universal+12, height-b+2, 10, 10)
        fill('#543D29')
        rect(universal+28, height-b+3, 7, 20)
        universal += 50

def drawTrees():
    a = -5    #x-location of vertex
    b = 480-40   #y-location of vertex
    fill('#809848')
    while a < width: #draws trees
        triangle(a, b, a+20, b, a+10, b-40)
        a += 10
        
def drawBalloon():
    xlocation = 550
    fill('#A1A499')
    rect(xlocation-1, ylocation-40, 2, 40)
    fill(255, 0, 0)
    ellipse(xlocation, ylocation-40, 20, 25)

def drawStreet():
    fill('#A9A9A9')
    rect(0, height-20, width, 40)
    var = 0
    fill('#BDB76B')
    while var < width: #draw those little yellow lines on the street
        rect(var, 470, 20, 5)
        var += 30

def draw():
    global x
    global z
    global ylocation
    background('#8DC8FC')
    
# causes cloud 1 to move across the screen and resets x at 0 if x > 480
    if x-30 > (width+65): 
        x = 0
    x += 1

    # causes cloud 2 to move across the screen and resets z at 0 if z > 480    
    if z > (width+65):
        z = 0
    z += 2
    
    # causes the balloon to rise up, does not reset since the balloon should float up forever
    ylocation -= 1 

    drawMountain()
    drawSun()
    drawClouds()
    drawTrees()
    drawCabins()
    drawBalloon()
    drawStreet()
