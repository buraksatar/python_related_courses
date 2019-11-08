class Person(object): # Super class
  def __init__(self, name):
    self.name = name
  def greet(self):
    print ("Hi, I'm " + self.name + ".") # Super class does something

class Student(Person): # Subclass inheriting from the super class
  def __init__(self, name, degree):
    self.name = name
    self.degree = degree
    super().__init__(name) # calls constructor of super class
  def greet(self):
    super().greet() # calls method of super class
    print ("I am a " + self.degree + " student.")
  
student = Student("Ali", "PhD") # Create an object of the subclass
student.greet()