class Rectangle:
  def __init__(self, x1, y1, x2, y2): # class constructor
    if x1 < x2 and y1 > y2:
      self.x1 = x1 # class variable
      self.y1 = y1 # class variable
      self.x2 = x2 # class variable
      self.y2 = y2 # class variable
    else:
      print("Incorrect coordinates of the rectangle!")
        
  # write your code here
  def width(self):
    return abs(self.x2 - self.x1)
  def height(self):
    return abs(self.y2 - self.y1)