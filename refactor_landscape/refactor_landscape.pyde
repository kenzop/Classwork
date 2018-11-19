'''
This is a refactored version of the previous landscape sketch 
'Happy Little Accidents', thus why they look identical
'''
def setup():
    global x, y, z, balloonY
    size(640, 480)
    noStroke()
    x, y, z, balloonY = 0, height, 0, height
def draw():
    global x,y, z, balloonY
    background(135, 206, 250)
    
    draw_sun(50, 40)
    
    draw_Mountain(-100, y, 200, y, 60, 200)
    draw_Mountain(-20, y, 380, y, 180, 270)
    draw_Mountain(200, y, 480, y, 360, 300)
    draw_Mountain(400, y, 700, y, 550, 250)
    
    draw_cloud1(x, (y+25)/2, 75, 25) #bottom circle
    draw_cloud1(x, (y-25)/2, 75, 50) #top circle
    draw_cloud1(x-25, y/2, 75, 50) #left circle
    draw_cloud1(x+25, y/2, 75, 50) # right circle
    
    draw_cloud2(z+30, y-325, 75, 25) #bottom circle
    draw_cloud2(z+30, y-375, 75, 50) #top circle
    draw_cloud2(z-5, y-350, 75, 50) #left circle
    draw_cloud2(z+55, y-350, 75, 50) # right circle

    draw_trees(-5, 440)

    draw_cabins(50, 40, 0)

    draw_street(height-20, width, 0)
    
    draw_balloon(550, balloonY)

def draw_sun(sunX, sunY):
    fill(255, 255, 0)
    ellipse(sunX, sunY, 60, 60)

def draw_Mountain(x1, y1, x2, y2, x3, y3):
    fill('#D0CEBA')
    triangle(x1, y1, x2, y2, x3, y3)

def draw_cloud1(cloudX, cloudY, sizeX, sizeY):
    
    global x    
    fill('#FFFCF7')
    ellipse(cloudX, cloudY, sizeX, sizeY)
    # causes cloud 1 to move across the screen and resets x at 0 if x > 480    
    if x-30 > (width+75): 
        x = 0
    x += 0.5
    
def draw_cloud2(cloudX, cloudY, sizeX, sizeY):
    global z
    fill('#FFFCF7')
    ellipse(cloudX, cloudY, sizeX, sizeY)
    # causes cloud 2 to move across the screen and resets z at 0 if z > 480
    if z-30 > (width+75): 
        z = 0
    z += 1

def draw_trees(x, y):
    fill('#809848')
    while x < width: #draws trees
        triangle(x, y, x+20, y, x+10, y-40)
        x += 10

def draw_cabins(a, b, universal):
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

def draw_street(x, y, var):
    fill('#A9A9A9')
    rect(0, x, y, 40)
    fill('#BDB76B')
    while var < width: #draw those little yellow lines on the street
        rect(var, 470, 20, 5)
        var += 30

def draw_balloon(xlocation, ylocation):
    global balloonY
    fill('#A1A499')
    rect(xlocation-1, ylocation-40, 2, 40)
    fill(255, 0, 0)
    ellipse(xlocation, ylocation-40, 20, 25)
    # causes the balloon to rise up, does not reset since the 
    # balloon should float up forever
    balloonY -= 1 
