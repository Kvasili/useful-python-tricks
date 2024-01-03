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


shape = Polygon(5, "Pentagon", color="red", line_thickness=10)
shape.draw()


class Square(Polygon):
    def __init__(self):
        super().__init__(4, "square", color="blue", length=100, line_thickness=1)


Square = Square()
Square.draw()
