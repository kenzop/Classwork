import random
stars = []

for star in range(100): 
    stars.append([random.randint(0, 640), random.randint(0, 480)])

def setup():
    size(640, 480)

def draw():
    global stars
    background(0)
    noStroke()
    fill(255)
    
    if frameCount % 60 == 0:
        stars.append([-5, random.randint(0, 480)])


    i = 0
    for i in range(len(stars)):
        try:
            ellipse(stars[i][0], stars[i][1], 5, 5)
            stars[i][0] += 0.2
            if stars[i][0] > 650:
                stars.pop(i)
        except:
            break
