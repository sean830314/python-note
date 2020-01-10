"""
Intent

Flyweight is a structural design pattern that lets you fit more objects into the available amount of RAM by sharing common parts of state between multiple objects instead of 
keeping all of the data in each object.

*What is this pattern about?

This pattern aims to minimise the number of objects that are needed by
a program at run-time. A Flyweight is an object shared by multiple
contexts, and is indistinguishable from an object that is not shared.
The state of a Flyweight should not be affected by it's context, this
is known as its intrinsic state. The decoupling of the objects state
from the object's context, allows the Flyweight to be shared.

*What does this example do?

The example below sets-up an 'object pool' which stores initialised
objects. When a 'Card' is created it first checks to see if it already
exists instead of creating a new one. This aims to reduce the number of
objects initialised by the program.
"""
from random import randint
class Shape():
    def draw():
        pass

class Circle(Shape):

    def __init__(self, color):
        self.color = color
        self._x = None
        self._y = None
        self._radius = None

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        self._y = y

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius
    
    def draw(self):
        print("Circle: Draw() [Color : {},x : {},y : {},radius : {}".format(self.color, self._x, self._y, self._radius))

class ShapeFactory():
    
    def __init__(self):
        self.circleMap = {}
    
    def getCircle(self, color):
        circle = None
        if color not in self.circleMap:
            circle = Circle(color)
            self.circleMap[color] = circle
            print("Creating circle of color : {}".format(color))
        else:
            circle = self.circleMap[color]
        return circle

def main():
    color_list = ["Red", "Green", "Blue", "White", "Black"]
    factory = ShapeFactory()
    print("circleMap size",len(factory.circleMap))
    for i in range(20):
        circle = factory.getCircle(color_list[randint(0, len(color_list) - 1 )])
        circle.x = randint(0, 100)
        circle.y = randint(0, 100)
        circle.radius = 100
        circle.draw()
    print("circleMap size",len(factory.circleMap))
if __name__=='__main__':

    main()
