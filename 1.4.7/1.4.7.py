import random
import turtle
win = turtle.Screen()
win.title("1.4.7 project")
y = 1
l = 180
while y < 38:
    x = random.randrange(2)
    turtle.speed(0)
    if x == 1:
        r =  random.randint(0, 255)
        g =  random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.colormode(255)
        turtle.fillcolor((r, g, b))
        turtle.begin_fill()
        turtle.circle(l)
        turtle.end_fill()
        turtle.right(90)
        l -= 5
        y += 1
turtle.done()