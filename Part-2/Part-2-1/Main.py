import Circle, Square, Rectangle

# Driver code
c = Circle.Circle("cir1", "green")
print("Circle Area: " , str(c.calculate_area(12)))

sq = Square.Square("squ", "yellow")
print("Square Area: " + str(sq.calculate_area(3)))

re = Rectangle.Rectangle("rect", "orange", 45, 69)
print("Rectangle Area: " + str(re.calculate_area()))