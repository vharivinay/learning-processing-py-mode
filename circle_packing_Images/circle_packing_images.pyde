class Circle:
    def __init__(self, x_, y_, c_):
        self.x = x_
        self.y = y_
        self.r = 1
        self.c = c_
        self.growing = True
        
    def show(self):
        fill(self.c)
        stroke(self.c)
        ellipse(self.x, self.y, 2*self.r, 2*self.r)
        
    def grow(self):
        if self.growing:
            self.r = self.r + 0.25;
        
    def edges(self):
        return (self.x + self.r > width or self.x - self.r < 0 or self.y + self.r > height or self.y - self.r < 00)
        
def setup():
    global circles, img #, spots
    
    size(758,600)
    
    img = loadImage("starrynight_758x600.jpg")
    
    img.loadPixels()
            
    circles = []

def newCircle():
    global circles, img #, spots
    
    x = random(width) #spot.x
    y = random(height) #spot.y
    
    valid = True
    for c in circles:
        d = dist(x, y, c.x, c.y)
        if d < c.r:
            valid = False
            break
    if valid:
        index = int(x) + int(y) * img.width  
        col = img.pixels[index]     
        return Circle(x,y,col)
    else:
        return False
    
def draw():
    global circles, img
    background(0)
    
    total = 10
    count = 0
    attempts = 0
    while count < total:
        newCirc = newCircle()    
        if newCirc is not False:
            c = newCirc.c
            circles.append(newCirc)
            count += 1
        attempts += 1
        if attempts > 1000:
            noLoop()
            print(frameCount)
            print("FINISHED")
            break
    
    for c in circles:
        if c.growing:
            if c.edges():
                c.growing = False
            else:
                for other in circles:
                    if c is not other:
                        d = dist(c.x, c.y, other.x, other.y)
                        if d - 2 < c.r + other.r:
                            c.growing = False
                            break                
        c.show()
        c.grow()
    
    # saveFrame('output/starryCircles_######.png')
