import random
x, y, a = 30, 275, False                   #for cloud 1
p, q, b = 500, 400, False                  #for cloud 2
spoop = ''
pumpkin = ''
ghostY = 400
page = 1
rectx = 200
recty = 100
myFont = ''
pumpX = 640
def setup():
    global spoop, myFont, pumpkin
    size(640, 480)
    noStroke()
    myFont = createFont('SansSerif.bold', 16)
    pumpkin = loadImage('pumpkin.png')
    pumpkin.resize(40, 40)
    spoop = loadImage('ghost.png')
    spoop.resize(50, 50)

def keyPressed():
    global ghostY
    if keyCode == DOWN and ghostY < height-50:
        ghostY += 5
    elif keyCode == UP and ghostY > 300:
        ghostY -= 5
def drawSky(): #This took way too long
    fill('#F47E00') #Draws a rectangle with this color followed by other rectangles of different colors below it, making it appear like a sunset
    rect(0, 0, width, height)
    fill('#F46100')
    rect(0, 0, width, height-40)
    fill('#F43000')
    rect(0, 0, width, height-80)
    fill('#D6002A')
    rect(0, 0, width, height-120)
    fill('#D60063')
    rect(0, 0, width, height-160)
    fill('#AF0052')
    rect(0, 0, width, height-200)
    fill('#A80051')
    rect(0, 0, width, height-240)
    fill('#C90049')
    rect(0, 0, width, height-280)
    fill('#4A007F')
    rect(0, 0, width, height-320)
    fill('#2F0077')
    rect(0, 0, width, height-360)
    fill('#1C007A')
    rect(0, 0, width, height-400)
    fill('#00008B')
    rect(0, 0, width, height-440)

def drawClouds():
    global x
    global y
    fill('#eccab6') 
    #cloud 2
    ellipse(x, y+25, 75, 25) #bottom circle
    ellipse(x, y-25, 75, 50) #top circle
    ellipse(x-25, y, 75, 50) #left circle
    ellipse(x+25, y, 75, 50) # right circle
    #cloud 2
    ellipse(p, q+25, 75, 25) #bottom circle
    ellipse(p, q-25, 75, 50) #top circle
    ellipse(p-25, q, 75, 50) #left circle
    ellipse(p+25, q, 75, 50) # right circle
       
def drawSun():
    fill('#FFA100')
    ellipse(width/2, height, 200, 200)

def mousePressed():
    global rectx, recty, page
    if mouseX > width/2-(rectx/2) and mouseX < width/2+(rectx/2) and mouseY > height-200 and mouseY <height+recty:
        page = 2

def page1():
    global rectx, recty
    background('#FF9100')
    textFont(myFont)
    textSize(40)
    fill('#bb0a1e') 
    text("Ghost Dodgers", width/2-150, height/4)
    fill(0, 255, 0)
    rect(width/2-(rectx/2), height-200, rectx, recty, 5)
    fill(255)
    textSize(17)
    text("Click here to Start", rectx+35, height-recty-40)
    text("Use the up and down keys to move the ghost.  Try not to get hit!", 15, height-250)

def page2():
    global x, a, p, b, spoop, pumpX
    drawSky()
    drawSun()
    drawClouds()
    image(spoop, 20, ghostY)
    while pumpX > -50:
        pumpY = random.randint(300, 480)
        image(pumpkin, pumpX, pumpY)
        pumpX -= 4
    print(pumpY)
 #To make cloud 1 move:
    if x > 700 and a == False:
        a = True
    
    if a == True and x < -40:
        x += 2
        a = False
    elif a == True:
        x -= 2
    else:
        x += 2
     #To make cloud 2 move:
    if p < -40 and b == False:
        b = True
    
    if b == True and p > 700:
        p -= 2
        b = False
    elif b == True:
        p += 2
    else:
        p -= 2

def draw():
    if page == 1:
        page1()
    elif page == 2:
        page2()
