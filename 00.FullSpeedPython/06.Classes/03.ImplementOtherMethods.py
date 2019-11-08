class Rectangle:
  def __init__(self, x1, y1, x2, y2): # class constructor
    if x1<x2 and y1>y2:
      self.x1 = x1 # class variable
      self.y1 = y1 # class variable
      self.x2 = x2 # class variable
      self.y2 = y2 # class variable
    else:
      print("Incorrect coordinates of the rectangle!")
        
  def width(self):
    return self.x2-self.x1
      
  def height(self):
    return self.y1-self.y2
  
  def area(self):
    return self.width()*self.height()
  
  def perimeter(self):
    return 2 * self.width() + 2 * self.height()

# test your code
r = Rectangle (2, 7, 8, 4)
print("Area: " + str(r.area()))
print("Perimeter: " + str(r.perimeter()))

# write your code here
  def __str__(self):
    return str(self.x1) + ', ' + str(self.y1) + ', ' + str(self.x2) + ', ' + str(self.y2)

#alternatively
def __repr__(self):
    return(str(self.x1) + ', ' + str(self.y1) + ', ' + str(self.x2) + ', '+str(self.y2))
  