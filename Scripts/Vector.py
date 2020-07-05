from math import sqrt

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def len(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def normalized(self):
        if self.len() == 0:
            return Vector()
        return Vector(self.x / self.len(), self.y / self.len())

    # operator overloading
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    # Print overload
    def __str__(self):
        return "x: {}, y {}".format(self.x, self.y)
