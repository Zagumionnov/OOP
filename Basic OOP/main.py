import math


class Shape:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render(self, color):
        print(f'Rendered with color {color}')

    def scale(self, scale_factor):
        print(f'Scaled with scale_factor {scale_factor}')

    def square(self):
        print('Hello from square()')

    def centre(self):
        return self.x, self.y

    def greater_than(self, other):
        return self.square() < other.square()

    def __gt__(self, other):
        return self.greater_than(other)

    def __contains__(self, item):
        return True




class Rectangle(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        square = self.height * self.width
        return square

    def print_sides(self):
        print(self.height, self.width)


class Circle(Shape):

    # def __init__(self, x, y radius):
    #     super().__init__(x, y)  ---> Shape.__init__(self, x, y)
    #     self.radius = radius
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        square = math.pi * self.radius ** 2
        return square

class Parallelogram(Rectangle):

    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle
        self.width2 = self.width * math.sin(math.radians(self.width))

    def square(self):
        square = self.width * self.width2
        return round(square, 2)

    def print_angle(self):
        print(self.angle)

    def __str__(self):
        return f'Parallelogram: {self.width}, {round(self.width2, 2)}, {self.angle}'



# s = Shape(10, 20)
# print(s.x, s.y)
#
# s = Shape(11, 21)
# print(s.x, s.y)
#
# s.render('RED')
# s.scale(0.5)
#
# r = Rectangle(1, 1, 2, 2)
# print(r.x, r.y, r.height, r.width)
#
# c = Circle(2, 2, 32)
# print(c.scale(1.2), c.x, c.y)
#
# p = Parallelogram(1, 1, 10, 20, 45)
#
# print()
#
# p.print_angle()
# p.print_sides()

r = Rectangle(1, 1, 10, 10)
print(r.square())

p = Parallelogram(1, 1, 10, 10, 30)
p1 = Parallelogram(1, 1, 19, 19, 32)
print(p.square())
print(p.greater_than(p1))
print(p in p1)

c = Circle(1, 1, 10)
print(c.square())

print(p)
