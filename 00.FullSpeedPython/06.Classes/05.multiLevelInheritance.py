class Animal ():
  def __init__(self, name, food, characteristic): # Animal's constructor
    self.name = name # Animal's attribute
    self.characteristic = characteristic # Animal's attribute
    self.food = food # Animal's attribute
    print ("I am a " + str(self.name) + ".")
    
class Mammal (Animal): # Mammal inherits from Animal
  def __init__(self, name, food): # Mammal's constructor
    Animal.__init__(self, name, food, "warm blooded") # Animal's constructor
    print ("I am warm blooded.")
    
class Carnivore (Mammal): # Carnivore inherits from Mammal
  def __init__(self, name): # Carnivore's constructor
    Mammal.__init__(self, name, "meat") # Mammal's constructor 
    print ("I eat meat.")

lion = Carnivore("lion") # lion is an instance of Carnivore