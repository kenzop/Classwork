import random
stars = []

for star in range(100):
    x = [random.randint(0, 640)]
    y = [random.randint(0, 480)] 
    stars.append([x, y])

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
            ellipse(float(str(stars[i][0])[1:-1]), float(str(stars[i][1])[1:-1]), 5, 5)
            a = str(float(str(stars[i][0])[1:-1])+0.2)
            stars[i][0] = "[{}]".format(a)
            if float(str(stars[i][0])[1:-1]) > 650:
                stars.pop(i)
        print(len(stars))
        except:
            break
