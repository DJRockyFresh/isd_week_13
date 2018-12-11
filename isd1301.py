#main code

class Shapes(object):
    def __init__ (self):
        def Radius(self):
            return False
    def Side(self):
        return False

class Circle(Shapes):
    def __init__ (self, radius):
        self.radius = radius
    def Radius(self):
        return True
    def area(self):
        return self.radius * self.radius * 3.14

class Rectangle(Shapes):
    def __init__ (self, shortSide, longSide):
        self.shortSide = shortSide
        self.longSide = longSide
    def Side(self):
        return False
    def area(self):
        return self.shortSide * self.longSide

class Square(Shapes):
    def __init__ (self, side):
        self.side = side
    def Side(self):
        return False
    def area(self):
        return self.side * self.side

class Ellipse(Shapes):
    def __init__ (self, shortRadius, longRadius):
        self.shortRadius = shortRadius
        self.longRadius = longRadius
    def Radius(self):
        return True
    def area(self):
        return self.shortRadius * self.longRadius * 3.14

#examples

crcl1 = Circle(4)
print("Since the radus of crc1 is ",crcl1.radius, ", the area will be", crcl1.area())

rctngl1 = Rectangle(128, 2)
print("Since values of rctngl1 are ",rctngl1.shortSide, " and ", rctngl1.longSide, ", the area will be", rctngl1.area())

sqr1 = Square(16)
print("Since a side of sqr1 equals",sqr1.side, "the area will b", sqr1.area())

llps1 = Ellipse(3, 9)
print("Values of shortRadius and longRadius are", llps1.shortRadius, "and", llps1.longRadius, ", the area is", llps1.area())


        
    
