import random
x, y, a = 30, 275, False                   #for cloud 1
p, q, b = 500, 400, False                  #for cloud 2
spoop = ''                                 #ghost
pumpkin = ''
ghostX = 20
ghostY = 400
page = 3
rectx = 200                                # X coordinate of the button
recty = 100                                # Y coordinate of the button 
myFont = ''
pumpX1 = 680
pumpY1 = 500
pumpX2 = 700
pumpY2 = 500
timer = 0
slowincrease1 = 0                          #Causes pumpkin 1 to speed up
slowincrease2 = 0                          #Causes pumpkin 2 to speed up
score = 0

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
        ghostY += 7
    elif keyCode == UP and ghostY > 300:
        ghostY -= 7
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
    if page == 1 and mouseX > width/2-(rectx/2) and mouseX < width/2+(rectx/2) and mouseY > height-200 and mouseY <height+recty:
        page = 2
    if page == 3:
        page = 1

def page1():
    global rectx, recty, timer, score, slowincrease1, slowincrease2, pumpX1, pumpX2
    background('#FF9100')
    textFont(myFont)
    textSize(40)
    fill('#bb0a1e') 
    text("Ghost Rush", width/2-132, height/4)
    fill(0, 255, 0)
    rect(width/2-(rectx/2), height-200, rectx, recty, 5)
    fill(255)
    textSize(16)
    text("Click here to Start", rectx+45, height-recty-40)
    text("Use the up and down keys to move the ghost.", 120, height-250)
    text("Try to get as many pumpkins as you can before time runs out!", 35, height-235)
    timer = 250 #Resets timer just in case player wants to play again
    score = 0 #Resets score
    slowincrease1 = 0
    slowincrease2 = 0
    pumpX1 = 680
    pumpX2 = 700
    if mouseX > width/2-(rectx/2) and mouseX < width/2+(rectx/2) and mouseY > height-200 and mouseY <height+recty:
        fill(0,128,0)
        rect(width/2-(rectx/2), height-200, rectx, recty, 5)
        fill(255)
        textSize(16)
        text("Click here to Start", rectx+45, height-recty-40)
        

def page3():
    background(0)
    fill(255)
    textSize(30)
    text("Game over.  Your score is: " + str(score), 125, 200)
    text("Click anywhere to reset", 150, 230)

def draw():
    global x, a, p, b, spoop, pumpX1, pumpY1, pumpX2, pumpY2, ghostX, timer, slowincrease1, slowincrease2, score, page

    if page == 1:
        page1()
    elif page == 2:
        if timer <= 0:
            page = 3
        drawSky()
        drawSun()
        drawClouds()
        image(spoop, ghostX, ghostY)
        image(pumpkin, pumpX1, pumpY1)
        image(pumpkin, pumpX2, pumpY2)

        if pumpX1 < -50 or pumpX1 > width:
            pumpY1 = random.randint(300, 440)
        if pumpX1 < -50:
            pumpX1 = width+20
            if slowincrease1 < 9:
                slowincrease1 += 0.5
        if pumpX1 > -10 and pumpX1 < ghostX + 20 and pumpY1 > ghostY-25 and pumpY1 < ghostY+28:
            score += 1
            pumpX1 = -50
        pumpX1 -= (4+slowincrease1)
        
        if pumpX2 < -10 or pumpX2 > width:
            pumpY2 = random.randint(300, 440)
        if pumpX2 < -50:
            pumpX2 = width+20
            if slowincrease2 < 7:
                slowincrease2 += 1
        if pumpX2 > -10 and pumpX2 < ghostX + 20 and pumpY2 > ghostY-25 and pumpY2 < ghostY+28:
            score += 1
            pumpX2 = -50
        if slowincrease1 > 7.5:
            pumpX2 -= (4+slowincrease2)
    
        timer -= 0.1
        text("timer:" + str(int(timer)), 450, 20)
        text("score:" + str(score), 150, 20)
                
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
    elif page == 3:
        page3()
