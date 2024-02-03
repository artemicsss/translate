def setup():
    size(600,600)
    background(0)
def draw():
    point(random(0,600),random(0,600))
    stroke(255,255,255)
    strokeWeight(3)
    fill(random(0,255),random(0,255),random(0,255))
    triangle(300,50,150,150,450,150)
    translate(0,100)
    triangle(300,50,150,150,450,150)
    translate(0,100)
    triangle(300,50,150,150,450,150)


    
