total_degrees = 360
angle = 0

cr = 0

r = 255
g = 69
b = 0

radius = 0

def setup():
    global displayWidth, displayHeight, radius
    size(displayWidth, displayHeight)
    background(0)
    colorMode(HSB)
    stroke(255, 25)
    noFill()
    
    radius = 0
    
def draw():
    global r, g, b, total_degrees, radius, angle, cr
    # background(0)
    # radius = height/2
    cx = width/2
    cy = height/2
    
    
    push()
    translate(displayWidth/2, displayHeight/2)
    rotate(radians(angle + 1))
    
    # stroke(r,cr,b)
    stroke(cr, 255, 255, 100)
    beginShape()
    for i in range(total_degrees):
        nF = noise(i * 0.03, float(frameCount)/60)
        # nF = map(nn,0,total_degrees,0,radius)
        x = radius * cos(radians(i)) * nF
        y = radius * sin(radians(i)) * nF
        curveVertex(x, y)
    endShape(CLOSE)
    pop()
    if radius >= 1.25 * width:
        run = floor(random(100000))
        saveFrame('Wallpaper/floweryboi_#####'+str(run)+'.png')
        noLoop()
    if cr >= 255:
        cr = 0
    # if angle >= 200:
    #     noLoop()
    radius = radius + 3
    angle = angle + 0.25
    cr = cr + 1
    
    # saveFrame('outputs/floweryboi_#####.png')
