class Animal():
    def __init__ (self, name, lifespan):
        self.name = name
        self.lifespan = lifespan
    def details (self):
        print("Name: ",self.name, "Lifespan: ", self.lifespan)

class Mammal(Animal):
    def __init__ (self, name, lifespan, species):
        Animal.__init__(self, name, lifespan)
        self.species = species
        print("Species: ", self.species)
        
class Insect(Animal):
    def __init__ (self, name, lifespan, species, size):
        Animal.__init__(self, name, lifespan)
        self.species = species
        self.size = size
        print("Species: ", self.species,)

anml1 = Mammal("Dog", "13 years", "Mammal")
print(anml1.name,",", anml1.lifespan)

print("---------------------------------------")

inc1 = Insect("Bee", "150 days", "Incect", "10 cm")
print(inc1.name,",", inc1.lifespan, ",", inc1.size)
        





