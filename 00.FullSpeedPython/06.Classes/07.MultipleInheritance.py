class Person:
  def __init__(self, name):
      self.name = name

  def greet(self):
    print("Hi, I am " + self.name + ".")


class Student (Person): # Student inherits from Person class
  def __init__(self, name, rollNumber):
    self.name = name # Attribute inherited from the Person class
    self.rollNumber = rollNumber # Student's attribute
    Person.__init__(self, name) # Person's constructor

  def report(self): # Student's method
    print("My roll number is " + self.rollNumber + ".")

class Teacher (Person): # Teacher inherits from Person class
  def __init__(self, name, course):
    self.name = name # Attribute inherited from the Person class
    self.course = course # Teacher's attribute
    Person.__init__(self, name) # Person's constructor   

  def introduce(self): # Teacher's method
    print("I teach " + self.course + ".")

class TA (Student, Teacher): # TA inherits from Student and Teacher class
  def __init__(self, name, rollNumber, course, grade):
    self.name = name # Attribute inherited from the Person class
    self.rollNumber = rollNumber # Attribute inherited from the Student class
    self.course = course # Attribute inherited from the Teacher class
    self.grade = grade # TA's attribute
    
  def details(self): # TA's method
    if self.grade=="A*" or self.grade=="A" or self.grade=="A-": # if person is elligible for TAship
      Person.greet(self) # can access Person's greet method
      Student.report(self) # can access Student's report method
      Teacher.introduce(self) # can access Teacher's introduce method
      print ("I got an " + self.grade + " in " + self.course + ".")
    else: # person is not elligible for TAship
      print(self.name + ", you can not apply for TAship.")
    
ta = TA('Ali', '13K-1234', 'Data Structures' ,'A') # TA object
ta.details()

#uncomment any of the following lines of code and see how they work
# ta.greet()
# ta.report()
# ta.introduce()

print("\n")

ta2 = TA('Ahmed', '14K-5678', 'Algorithms' ,'B')
ta2.details()