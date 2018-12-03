def setup():
    global megaman_still, megaman_still_left, megaman_run, megaman_run_left, rectx, recty
    global TIME, PAGE, MEGAMAN, MEGAMANX, MEGAMANY
    size(640, 480)
    megaman_still = loadImage('megaman_still.png')
    megaman_still.resize(200, 100)
    megaman_run = loadImage('megaman_run.png')
    megaman_run.resize(200, 100)
    megaman_still_left = loadImage('megaman_still_left.png')
    megaman_still_left.resize(200, 100)
    megaman_run_left = loadImage('megaman_run_left.png')
    megaman_run_left.resize(200, 100)
    rectx = 200
    recty = 100
    
    TIME = 0
    PAGE = 1    
    MEGAMAN = megaman_still
    MEGAMANX = 50
    MEGAMANY = 300
    

# Used to track user inputs and move megaman accordingly
def keyPressed():
    global MEGAMANX, TIME
    if keyCode == RIGHT:
        MEGAMANX += 2
        TIME += 1
    if keyCode == LEFT:
        MEGAMANX -= 2
        TIME += 1

# Used to check the mouse's location.  This is used on the intro screen 
# to either take the player to the main game or to the instructions
def mousePressed():
    global rectx, recty, PAGE
    if PAGE == 1 and mouseX > width/4-(rectx/2) and mouseX < width/4+(rectx/2) and mouseY > height-200 and mouseY <height+recty:
        PAGE = 3


# This function determines what image of megaman to show to give the impression of
# an animation
def megaman_movements():
    global TIME, MEGAMAN
    if TIME > 2 and keyCode == RIGHT:
        MEGAMAN = megaman_run
    elif TIME <= 2 and keyCode == RIGHT: 
        MEGAMAN = megaman_still
    if TIME > 2 and keyCode == LEFT:
        MEGAMAN = megaman_run_left
    elif TIME < 2 and keyCode == LEFT: 
        MEGAMAN = megaman_still_left
    if TIME > 4:
        TIME = 0

def level1_spikes(x, y, midpoint):
    while x < 300:
        fill(119,136,153)
        triangle(x, y, x+midpoint*2, y, x+midpoint, y) #FIX
        x += 30

# What the program will display while the user is on the introduction scene
def page1():
    # Code for start button.  Changes color to a darker shade of green if the
    # mouse hovers over it
    fill(0, 255, 0)
    rect(width/4-(rectx/2), height-200, rectx, recty, 5)
    textSize(16)
    fill(255)
    text("Click here to Start", rectx-110, height-recty-40)

    if mouseX > width/4-(rectx/2) and mouseX < width/4+(rectx/2) and mouseY > height-200 and mouseY <height+recty:
        fill(0,128,0)
        rect(width/4-(rectx/2), height-200, rectx, recty, 5)
        fill(255)
        text("Click here to Start", rectx-110, height-recty-40)

# What the player sees on level 1
def page3():
    background(255)
    megaman_movements()
    image(MEGAMAN, MEGAMANX, MEGAMANY)
    level1_spikes(200, 300, 15)
def draw():
    if PAGE == 1:
        page1()
    elif PAGE == 3:
        page3()  
