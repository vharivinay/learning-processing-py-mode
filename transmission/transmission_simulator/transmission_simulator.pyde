w = 1280
h = 720
num_people = 500

class Ball(object):
    global w, h

    def __init__(self, xp, yp, xv, yv):
        self.x = xp
        self.y = yp
        self.vx = xv
        self.vy = yv

    def move(self):
        if self.x < 0 or self.x > w:
            self.vx *= -1
        if self.y < 0 or self.y > h:
            self.vy *= -1
        self.x += self.vx
        self.y += self.vy
        return

    def display(self):
        fill(151)
        ellipse(self.x,self.y,3,3)

class Person(Ball):
    global people, num_people

    def __init__(self,id, xp, yp, xv, yv, status):
        super(Person,self).__init__(xp, yp, xv, yv)
        self.id = id
        self.status = status

    def display(self):
        if self.status == 'unexposed':
            fill(151)
        elif self.status == 'exposed':
            fill(255,0,0)
        ellipse(self.x,self.y,3,3)

    def transmit(self):
        for i in range(num_people):
            dx = self.x -people[i].x
            dy = self.y -people[i].y
            d_sqr = dx*dx + dy*dy
            if d_sqr < 200:
                if self.status=='exposed' and people[i].status=='unexposed':
                    people[i].status = 'exposed'
                elif self.status=='unexposed' and people[i].status=='exposed':
                    self.status = 'exposed'

people = []
for i in range(num_people):
    people.append(Person(id,random(w),random(h), random(-10,10), random(-10,10),'unexposed'))

people[0].status = 'exposed'

def setup():
    global w, h
    size(w,h)
    background(51)

def draw():
    background(51)
    for i in range(num_people):
        people[i].move()
        people[i].transmit()
        people[i].display()
