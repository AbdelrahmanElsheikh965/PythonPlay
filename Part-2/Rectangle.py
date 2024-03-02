'''
    Define a class named Shape with attributes name and _color (private).
    Implement encapsulation by providing methods get_color() and set_color(color).
    Include an abstract method calculate_area() in the Shape class.
    Create two subclasses, Circle and Square, each inheriting from Shape.
    Implement polymorphism by overriding the calculate_area() method in the subclasses.
    Create another subclass, Rectangle, inheriting from Shape with additional attributes such as length and width.
    print the calculate_area for Circle, Square and Rectangle "assume length = width = 5 as inputs"
'''

import Shape 

class Rectangle(Shape.Shape):
  def __init__(self, name, _color, length, width):
    super().__init__(name, _color)
    self.length = length
    self.width = width
  
  def calculate_area(self):
    return self.length * self.width
    
  