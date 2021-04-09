num_stars = 600
x = 0
y = 0
z = 0

pz = 0

w = 1000
h = 1000
speed = 10

def setup():
    global w, h
    size(w,h)
    colorMode(RGB)
    background(0)

class stars(object):
    global w, h, speed, pz

    def __init__(self, x, y, z):
        self.x = random(-w,w)
        self.y = random(-h,h)
        self.z = random(w)
        pz = self.z
    
    def move(self):
        speed = 20# map(mouseX,0,w,0, 25)
        self.z = self.z - speed
        if self.z < 1:
            self.z = width/2
            self.x = random(-w/2,w/2)
            self.y = random(-h/2,h/2)
            pz = self.z

    def display(self):
        
        noStroke
        fill(255)
        
        sx = map(self.x/self.z,0,1,0,w/2)
        sy = map(self.y/self.z,0,1,0,h/2)
        r = map(self.z,0,w/2,2,0)
        pz = self.z
        
        ellipse(sx,sy,r,r)
        l1 = 0.5
        l2 = 0.9
        px = map(self.x*l1/pz,0,1,0,w/2)
        py = map(self.y*l1/pz,0,1,0,h/2)
        
        rc = map(self.z,0,w,0,255)
        bc = map(self.z,0,h,255,0)
        
        strokeWeight(1)
        # stroke(rc,0,bc)
        stroke(255)
        line(px*l2, py*l2, sx*l1, sy*l1)

starry = []

for i in range(num_stars):
    starry.append(stars(x,y,z))

r = 255
b = 0

def draw():
    global r, b
    
    background(0)
    translate(w/2, h/2)
    
    for i in range(num_stars):
        starry[i].move()
        starry[i].display()
    
   #  saveFrame('starflow/hyperspace#####.png')
    
    if frameCount > 1000:
        noLoop()
    print(frameRate)
