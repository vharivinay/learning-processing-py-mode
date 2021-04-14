def setup():
    global width, height, n, p
    
    size(700,700)
    background(0)
    translate(width/2,height/2)
    
    offset = 100
    w = width-offset
    h = height-offset
    
    n = 5
    p = PVector(random(w),random(h))
    
def shapeUpdate(n_):
    global width, height, shapes, n, p
        
    offset = 100
    w = width-offset
    h = height-offset
    
    n = n_
    shapes = []
    
    stroke(255)
    strokeWeight(1)
    
    for i in range(n):
        a = i * TWO_PI/n
        v = PVector(w*0.5*cos(a),h*0.5*sin(a))
        shapes.append(v)
        point(v.x,v.y)
    
    return shapes
    
def newPoint(shapes_):
    global width, height, n, p
    
    points = []
    l = 0.45
    rold = 0
    
    for i in range(2500):
        r = floor(random(n))
        if n > 3:
            if not(r==rold):
                q1 = lerp(shapes[r].x,p.x,l)
                q2 = lerp(shapes[r].y,p.y,l)
                q = PVector(q1,q2)
                points.append(q)
                p.set(q)
                rold = r
        else:
            q1 = lerp(shapes[r].x,p.x,l)
            q2 = lerp(shapes[r].y,p.y,l)
            q = PVector(q1,q2)
            points.append(q)
            p.set(q)

    return points

nn = 3

def draw():
    global width, height, shapes, n, p, nn
    
    translate(width/2, height/2)
    
    if frameCount%300 == 0:
        nn = nn + 1
        background(0)
    
    if frameCount > 2399:
        noLoop()
        
    shapes = shapeUpdate(nn)
    points = newPoint(shapes)
    
    stroke(255,255,255,50)
    strokeWeight(1)
    
    for i in points:
        point(i.x,i.y)
    
    # saveFrame('frames/fractal_####.png')
    
    print(frameCount)
