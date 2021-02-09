from abc import ABC
class Shape(ABC): #abstract class shape class is the inherited class of ABC
    def calculate_area(self): 
        #abstract method
        pass

class Rectangle(Shape): # Rectangle is a subclass of Shape(inherited class)
  length = 5
  breadth = 3
  def calculate_area(self):
      return self.length * self.breadth

class Circle(Shape): # Circle is a subclass of Shape(inheried class)
  radius = 4
  def calculate_area(self):
      return 3.14 * self.radius * self.radius

rec = Rectangle() #object created for the class 'Rectangle'
cir = Circle() #object created for the class 'Circle'
print("Area of a rectangle:", rec.calculate_area()) #call to 'calculate_area' method defined inside the class 'Rectangle'
print("Area of a circle:", cir.calculate_area()) #call to 'calculate_area' method defined inside the class 'Circle'.
# Output:
# Area of a rectangle: 15
# Area of a circle: 50.24
from abc import ABC
class Shape(ABC): #abstract class shape class is the inherited class of ABC
    def calculate_area(self): 
        #abstract method
        pass

class Rectangle(Shape): # Rectangle is a subclass of Shape(inherited class)
  length = 5
  breadth = 3
  def calculate_area(self):
      return self.length * self.breadth

class Circle(Shape): # Circle is a subclass of Shape(inheried class)
  radius = 4
  def calculate_area(self):
      return 3.14 * self.radius * self.radius

rec = Rectangle() #object created for the class 'Rectangle'
cir = Circle() #object created for the class 'Circle'
print("Area of a rectangle:", rec.calculate_area()) #call to 'calculate_area' method defined inside the class 'Rectangle'
print("Area of a circle:", cir.calculate_area()) #call to 'calculate_area' method defined inside the class 'Circle'.
# Output:
# Area of a rectangle: 15
# Area of a circle: 50.24