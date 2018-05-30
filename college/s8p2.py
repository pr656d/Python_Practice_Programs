# Define a class name circle which can be constructed using a parameter radius.
# The class has a method which can compute the area using area method.


class Circle:
    radius = 0

    def __init__(self, radius):
        self.radius = radius

    def displayArea(self):
        print("Area:", (3.14 * (self.radius ** 2)))


a1 = Circle(5)
a1.displayArea()
