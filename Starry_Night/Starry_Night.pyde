import random
stars = []

for star in range(100):
    x = [random.randint(0, 640)]
    y = [random.randint(0, 480)] 
    stars.append([x, y])

def setup():
    size(640, 480)

def draw():
    background(0)
    noStroke()
    fill(255)
    
    if frameCount % 60 == 0:
        stars.append([-5, random.randint(0, 480)])

    index = 0
    '''
    ???????????????????/????/
    i = 0
    for i in range(len(stars)):
        a = str(stars[i][0])
        a = int(a[1:-1])
        b = str(stars[i][1])
        b = int(b[1:-1])        
    '''
    for index in range(len(stars)):
        try:
            #this ellipse ting is bug problem. Plz fix boi
            ellipse(stars[index][0], stars[index][1], 5, 5)
            stars[index][0] += 0.2
            if stars[index][0] > 650:
                stars.pop(index)
        except:
            break
