class Animal(object):
    def __init__ (self, subclass):
        self.subclass = subclass
    def getName (self):
        return self.name

class Mammal(Animal):
    def __init__ (self, subclass):
        

class Insect(Animal):
    def __init__ (self, ):

class Dog(Mammal):
    def __init__ (self, ):

class Bee(Insect):
    def __init__ (self, ):

