x = 200
y = 200

def setup():
    size(displayWidth/2, displayHeight)
    background(0)
      
    colorMode(HSB)
    global x, y

    x = width/2
    y = height/2

hu = 0
step = 5
count = 0
p1 = []

def decide():
    global x, y
    r = floor(random(0,4))

    if r == 0:
        x = x+step
    elif r == 1:
        x = x-step
    elif r == 2:
        y = y+step
    else:
        y = y-step
    
    return(x,y)

def check_visited(p):
    global x, y
    var = True
    while var:
        if p in p1:
            p = decide()
        else:
            var = False
    return (x,y)

def draw():
    
    global x, y, r, g, b, hu, step, count, p1
    
    if count > 10000:
        noLoop()
    
    
    stroke(hu,255,255)
    noFill()
    strokeWeight(step+1)
    
    p = decide()
    
    p1.append(p)
    
    p = check_visited(p)
    
    beginShape()
    vertex(p[0],p[1])
    endShape()
    
    # saveFrame('outputs/walk_#####.png')
    
    if hu >= 255:
        hu = 0
    
    hu += 0.1
    count += 1
    
    if count%1000 == 0:
        print(count)
