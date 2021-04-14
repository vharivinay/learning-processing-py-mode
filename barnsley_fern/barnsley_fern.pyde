'''
Total range: −2.1820 < x < 2.6558 and 0 ≤ y < 9.9983.

x0 = 0, y0 = 0

ƒ1 (p = 0.01)
xn + 1 = 0
yn + 1 = 0.16yn

ƒ2 (p = 0.85)
xn + 1 = 0.85xn + 0.04yn
yn + 1 = −0.04xn + 0.85yn + 1.6.

ƒ3 (p = 0.93)
xn + 1 = 0.2xn − 0.26yn
yn + 1 = 0.23xn + 0.22yn + 1.6.

ƒ4 (else)
xn + 1 = −0.15xn + 0.28yn
yn + 1 = 0.26xn + 0.24yn + 0.44.

'''

x = 0
y = 0

def setup():
    global width, height
    size(1000,1000)
    background(0)
    colorMode(HSB)
    
def drawPoint():
    global width, height, x, y
    
    dx = map(x, -2.1820, 2.6558, 0.2*width, 0.8*width)
    dy = map(y, 0, 9.9983, height, 0)
    
    hu = map(dy, 0, height, 0, 200)
    
    stroke(hu,255,255)
    strokeWeight(0.5)
    
    point(dx, dy)
    
def nextPoint():
    global width, height, x, y
    
    r = random(1)
    
    if r < 0.01:
        nx = 0
        ny = 0.016 * y
    elif r < 0.85:
        nx = 0.85 * x + 0.04 * y
        ny = -0.04 * x + 0.85 * y + 1.6
    elif r < 0.93:
        nx = 0.20 * x - 0.26 * y
        ny = 0.23 * x + 0.22 * y + 1.6
    else:
        nx = -0.15 * x + 0.28 * y
        ny = 0.26 * x + 0.24 * y + 0.44
    
    x = nx
    y = ny
    
def draw():
    for i in range(250):
        drawPoint()
        nextPoint()
    
    # saveFrame('fern/fern_####.png')
    
    if frameCount > 2999:
        noLoop()
    print(frameCount)
