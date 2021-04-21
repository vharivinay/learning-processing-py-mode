class Particle:
    global snowFlake, width
    
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.rad = 3
        
    def update(self):
        self.pos.x -= 0.5
        self.pos.y += random(-3,3)
        
        angle = self.pos.heading()
        angle = constrain(angle, 0, PI/6)
        magnitude = self.pos.mag()
        self.pos = PVector.fromAngle(angle)
        self.pos.setMag(magnitude)
        
    def show(self):
        # noFill()
        hu = dist(0,0,self.pos.x,self.pos.y)
        hu = map(hu,0,width/2,100,255)
        fill(hu,255,255,225)
        noStroke()
        # stroke(hu,255,255,150)
        # strokeWeight(5)
        # point(self.pos.x,self.pos.y)
        ellipse(self.pos.x, self.pos.y, self.rad*2, self.rad*2)
        
    def finished(self):
        return self.pos.x < 1
    
    def intersects(self, snowFlake):
        result = False
        for flake in snowFlake:
            d = dist(flake.pos.x,flake.pos.y,self.pos.x,self.pos.y)
            if d < self.rad:#*2 * 0.95:
                result = True
                break
        return result
        
                
def setup():
    global current, snowFlake, gap
    size(1000,1000)
    colorMode(RGB)
    snowFlake = []
    gap = 25
    current = Particle(width/2 - gap,random(0,10))
    
def draw():
    global current, snowFlake, gap
    
    translate(width/2,height/2)
    rotate(PI/6)
    background(0)
    
    # current.show()
    while not current.finished() and not current.intersects(snowFlake):
        current.update()
        
    snowFlake.append(current)
    current = Particle(width/2 - gap, 0)

    for i in range(6):
        rotate(PI/3)
        current.show()
        for flakes in snowFlake:
            flakes.show()
        
        pushMatrix()
        scale(1, -1)
        current.show()
        for flakes in snowFlake:
            flakes.show()
        popMatrix()
           
    # saveFrame('snowflakes/flakes_######.png')
