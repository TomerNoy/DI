import math


class Circle:

    def __init__(self):
        self.radius = 0
        self.diameter = 0

    def input_radius(self, radius):
        self.radius = radius
        self.diameter = radius * 2

    def input_diameter(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def get_area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f'circle r:{self.radius} d:{self.diameter} a:{round(self.get_area(), 2)}'

    def __add__(self, other):
        if type(other) is not Circle:
            raise TypeError('invalid Circle type')
        return self.get_area() + other.get_area()

    def __gt__(self, other):
        if type(other) is not Circle:
            raise TypeError('invalid Circle type')
        return self.get_area() > other.get_area()

    def __eq__(self, other):
        if type(other) is not Circle:
            raise TypeError('invalid Circle type')
        # print(self.get_area(), other.get_area())
        return self.get_area() == other.get_area()

    def __int__(self):
        return int(self.get_area())


c1 = Circle()
c2 = Circle()


c1.input_diameter(12)
c2.input_diameter(19)


print('test', c1, c2)

print(c1.radius, c1.diameter, c1.get_area())
print(c1)

print(c1 + c2)

print(c1 == c2)

circles = [c2, c1]

for c in circles:
    print(id(c))

circles.sort()

for c in circles:
    print(id(c))
