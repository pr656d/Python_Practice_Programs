import turtle
my_turtle = turtle.Turtle()
my_turtle.speed(0)

length = 100
angle = 90
rotate = 11

def square(length, angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)

def circle(length, angle):
    for i in range(100):
        square(length, angle)
        my_turtle.right(rotate)

circle(length, angle)
