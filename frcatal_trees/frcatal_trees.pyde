def setup():
    global width, height, hu
    size(1280,720)
    background(0)
    translate(width/2, height)
    colorMode(RGB)
    
def tree(len_):
    global width, height, hu
    
    # r = random(0.65,0.75)
    # angle = radians(random(10,75)) 
    lenfactor = 1

    stroke(165,42,42)
    strokeWeight(1)
    if len_ < 20:
        stroke(0,255,0)
    strokeWeight(len_/3.5)
    
    line(0,0,0,-len_)
    translate(0,-len_)
    if len_ > 3:
        push()
        angle = radians(random(10,75)) 
        rotate(angle)
        r = random(0.65,0.75)
        tree(len_ * lenfactor * r)
        pop()
        push()
        angle = radians(random(10,75)) 
        rotate(-angle)
        r = random(0.65,0.75)
        tree(len_ * lenfactor * r)
        pop()
    
def draw():
    global width, height
    
    background(0)
    translate(width/2, height)
    tree(200)
    
    # if frameCount < 40:
    #     saveFrame('trees/frcatalTrees_####.png')
    # else:
    #     noLoop()
