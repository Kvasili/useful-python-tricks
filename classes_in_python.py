'''

    python basics about classes
    check: 
    https://www.youtube.com/watch?v=tmY6FEF8f1o&ab_channel=KeithGalli


'''


import matplotlib.pyplot as plt
import turtle


class Polygon():

    ''' 
        This method is used to instantiate the class
        creates an object of the class 

    '''

    def __init__(self, sides, names, color, length=100, line_thickness=3):

        self.sides = sides
        self.names = names
        self.length = length
        self.color = color
        self.line_thickness = line_thickness

        self.interior_angles = (self.sides-2)*180
        self.angle = self.interior_angles/self.sides

    def draw(self):
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for i in range(self.sides):
            turtle.forward(self.length)
            turtle.right(180-self.angle)
        turtle.done()

        self.message = "Hello World!"


shape = Polygon(5, "Pentagon", color="red", line_thickness=10)
# shape.draw()


class Square(Polygon):
    def __init__(self):
        super().__init__(4, "square", color="blue", length=100, line_thickness=1)


# Square = Square()
# Square.draw()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        ''' operator overloading - we assume that other is a point like object which can be used
        for addition

        check:
         https://www.geeksforgeeks.org/operator-overloading-in-python/

         '''
        x = self.x + other.x
        y = self.y + other.y

        return Point(x, y)

    def plot(self):
        plt.scatter(self.x, self.y)
        plt.show()


# a = Point(1, 1)
# b = Point(10, 2)

# c = a+b
# print(c.x, c.y)
