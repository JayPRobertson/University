import math

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    
    def delta_y(self, d):
        return Point(self.x, self.y + d)
    
    def delta_x(self, d):
        return Point(self.x + d, self.y)
    
    def translate(self, d_x, d_y):
        return Point(self.x + d_x, self.y + d_y)
    
class Rectangle:
    
    def __init__(self, upper_left, lower_right):
        self.upper_left = upper_left
        self.lower_right = lower_right
    
    def __repr__(self):
        upl = self.upper_left
        lowr = self.lower_right
        return f'Rectangle(Point({upl.x}, {upl.y}), Point({lowr.x}, {lowr.y}))'
    
    def area(self):
        x = self.lower_right.x - self.upper_left.x
        y = self.upper_left.y - self.lower_right.y        
        return abs(x*y)
    
    def perimeter(self):
        x = abs(self.lower_right.x - self.upper_left.x)
        y = abs(self.upper_left.y - self.lower_right.y)   
        return 2*x + 2*y
    
    def translate(self, dx, dy):
        new_low = self.lower_right.translate(dx, dy)
        new_up = self.upper_left.translate(dx, dy)
        return Rectangle(new_up, new_low)
    
class Circle:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius
    
    def __repr__(self):
        r = self.radius
        c = self.centre
        return f'Circle({self.centre}, {self.radius})'
    
    def area(self):
        return math.pi * (self.radius)**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def translate(self, dx, dy):     
        return Circle(self.centre.translate(dx, dy), self.radius)    
    
