import math
class Calculator:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        return int(self.num1 / self.num2)


class AreaCalculator:

    def __init__(self,radius,num1, base, height):
        self.radius = radius
        self.num1 = num1
        self.base = base
        self.height = height

    def area_circle(self):
        return math.pi * self.radius**2

    def area_square(self):
        return self.num1**2

    def area_triangle(self):
        return (self.height * self.base)/2

