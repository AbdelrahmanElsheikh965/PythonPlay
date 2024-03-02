'''
    Define a class named Shape with attributes name and _color (private).
    Implement encapsulation by providing methods get_color() and set_color(color).
    Include an abstract method calculate_area() in the Shape class.
    Create two subclasses, Circle and Square, each inheriting from Shape.
    Implement polymorphism by overriding the calculate_area() method in the subclasses.
    Create another subclass, Rectangle, inheriting from Shape with additional attributes such as length and width.
    print the calculate_area for Circle, Square and Rectangle "assume length = width = 5 as inputs"
'''

from abc import ABC, abstractmethod

class Shape:
  
  def __init__(self, name, _color):
    self.__name = name  
    self.___color = _color
    
  def getColor(self):
    return self.___color
  
  def setColor(self, newColor):
    self.___color = newColor

  @abstractmethod
  def calculate_area():
    pass
    

# Shape.calculate_area()
# s = Shape("ahmed", "red")
# s.setColor("blue")
# print(s.getColor())