N = 200
 
damping = 0.995

def setup():
    
    global rows, cols, current, previous
    
    size(480,480)
    cols = width
    rows = height
    colorMode(RGB)
    current = [[0] * cols for i in range(rows)]
    previous = [[0] * cols for i in range(cols)]
    current[rows/2][cols/2] = 500
    
    
def mouseDragged():
  current[mouseX][mouseY] = 500
  
def mousePressed():
  current[rows/2][cols/2] = 500
  
  
def draw():
    global rows, cols, current, previous, damping
    background(0)
    # translate(rows/2,cols/2)
    loadPixels()
    for j in range(2,cols-2):
        for i in range(2,rows-2):
            current[i][j] = (previous[i-1][j]+
                            previous[i+1][j]+
                            previous[i][j-1]+
                            previous[i][j+1]) / 2 - current[i][j]
            current[i][j] = current[i][j] * damping
            
            index = j + i * cols
            pixels[index] = color(200*current[i][j])
            
    updatePixels()
    temp = current
    current = previous
    previous = temp
    
    saveFrame('outputs/ripple_#####.png')
        
    
    
            
                            
