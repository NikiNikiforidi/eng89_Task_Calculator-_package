from app.calculator import Calculator
from app.calculator import AreaCalculator


# Class Calculator argument syntax (num1, num2)

print(Calculator(10,4).addition())
print(Calculator(10,4).subtraction())
print(Calculator(10,4).multiplication())
print(Calculator(10,4).division())


# Class AreaCalculator argument syntax (radius,num1, base, height)
print(AreaCalculator(5,10,15,20).area_circle())
print(AreaCalculator(5,10,15,20).area_square())
print(AreaCalculator(5,10,15,20).area_triangle())
