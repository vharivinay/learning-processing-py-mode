fractal = []

def setup():
    global b, frcatal
    size(1000,1000, P3D)
    colorMode(RGB)
    b = Box(0, 0, 0, 300) 
    fractal.append(b)
    
class Box:
    
    def __init__(self, x, y, z, l):
        self.pos = PVector(x, y, z)
        self.l  = l
       
    def generate(self):
        boxes = []
        for x in range(-1,2):
            for y in range(-1,2):
                for z in range(-1,2):
                    sum = abs(x) + abs(y) + abs(z)
                    l = self.l/3
                    if sum > 1:
                        b = Box(self.pos.x + x * l, self.pos.y + y * l, self.pos.z + z * l, l)
                        boxes.append(b)
        return boxes
    
    def show(self):
        push()
        translate(self.pos.x, self.pos.y, self.pos.z)
        noStroke()
        fill(225)
        box(self.l)
        pop()

def subdivide():
    global fractal
    newBoxes = []
    for f in fractal:
        next = f.generate()
        newBoxes.extend(next)
    
    fractal = newBoxes
    
        
a = 0
def draw():
    global a, b, fractal
    background(0)
    stroke(255)
    noFill()
    lights()
    
    translate(width/2,height/2)
    rotateX(a)
    rotateY(a*0.4)
    rotateZ(a*0.1)
    for f in fractal:
        f.show()
    
    a += 0.01
    
    if frameCount%250 == 0:
        subdivide()
    
    if frameCount > 1200:
        noLoop()
    
    # saveFrame('menger/mengerSponge_####.png')
    
    print(frameCount)
