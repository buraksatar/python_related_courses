class Rectangle:
  # write your code here
  def __init__(self, x1, y1, x2, y2):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
    print('Rectangle(',x1,', ',y1,', ',x2,', ',y2,') created')

# Alternative Solutions
class Rectangle2:
  def __init__(self, x1, y1, x2, y2): # class constructor
    if x1 < x2 and y1 > y2:
      self.x1 = x1 # class variable
      self.y1 = y1 # class variable
      self.x2 = x2 # class variable
      self.y2 = y2 # class variable
    else:
      print("Incorrect coordinates of the rectangle!")
        
r = Rectangle2(2, 7, 8, 4)