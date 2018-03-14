import turtle

my_turtle = turtle.Turtle()

length = 100
angle = 90

# Defining a function
def square(length, angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)

square(length, angle)    # Calling a function
my_turtle.forward(length)
square(length, angle)
