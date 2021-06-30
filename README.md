# Package Calculator

### **TASK**
- 1) Build function containing add, subtract, multiply and divide
- 2) Build additional function for area of circle, square, triangle 
    

- -----------------------------------------------------
- Begin by creating new app directory and add `__init__.py` file and `calculator.py` file
- In normal folder create `program.py` file and `setup.py` file
**__init__.py**
  `empty`
  
**calculator.py**

```
import math    # Import math package to use pi

class Calculator:       # Create simple calculator using classes

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


class AreaCalculator:       # Creating calculator that calculates areas

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


```

**setup.py**
```
from setuptools import setup


setup(name="calc app")
version = "1.0"
description = "Simple calculator app"
author = "Niki at Sparta Global"
```
**program.py**
```
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

```
