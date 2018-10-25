x, y, a = 30, 275, False                   #for cloud 1
p, q, b = 500, 400, False                  #for cloud 2

def setup():
    size(640, 480)
    noStroke()

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

def drawSpoopyHouse():
    universal = 50 
    fill('#CA8F42')
    rect(universal, height-b, a, b)
    rect(universal+35, height-(b+18), 10, 20)
    fill('#B06660')
    triangle(universal, height-b, universal+50, height-b, universal+25, height-(b+20))
    fill('#5594ED')
    rect(universal+12, height-b+2, 10, 10)
    fill('#543D29')
    rect(universal+28, height-b+3, 7, 20)

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
def draw():
    global x
    global a
    global p
    global b
    drawSky()
    drawSun()
    drawClouds()
    drawSpoopyHouse
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
