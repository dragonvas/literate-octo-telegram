e=0
ee=0
def collideRectCircle(rx, ry, rw, rh, cx, cy, diameter): 
    testX = cx
    testY = cy
    if cx < rx:
        testX = rx
    elif cx > rx+rw:
        testX = rx+rw
    if cy < ry:
        testY = ry
    elif cy > ry+rh:
        testY = ry+rh
    distance = dist(cx,cy,testX,testY)
    if distance <= diameter/2:
        return True
    else:
        return False
def setup():
    size(800, 800)
    textSize(50)
def draw():
    global e,ee
    background(123,234,0)
    r1 = collideRectCircle(0,200, 600, 100, e, ee, 50)
    r2 = collideRectCircle(200,400, 600, 100, e, ee, 50)
    r3 = collideRectCircle(0,600, 600, 100, e, ee, 50)
    r4 = collideRectCircle(10,750, 30, 20, e, ee, 50)
    r5 = collideRectCircle(300,0, 50, 100, e, ee, 50)
    colide = r1 or r2 or r3
    rect(0,200, 600, 100)
    rect(200,400, 600, 100)
    rect(0,600, 600, 100)
    rect(10,750, 30, 20)
    rect(300,0, 50, 100)
    ellipse(e, ee, 50, 50)
    if keyPressed:
        if keyCode == UP:
            ee=ee-5
        if keyCode == DOWN:
            ee=ee+5
        if keyCode == LEFT:
            e=e-5
        if keyCode == RIGHT:
            e=e+5
    if colide == True:
        ee=ee-10
    if r4 == True:
        noLoop()
        background(123,234,0)
        text('YOU WIN',400,400)
    if r5 == True:
        e=e-10
        
    
