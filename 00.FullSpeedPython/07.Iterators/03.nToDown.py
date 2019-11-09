class MyRange:
  def __init__(self, n):
    self.n = n

  def __iter__(self):
    return self

  def next(self):
    #write your code here
    downArray = []
    for i in range(self.n+1):
      downArray.append(self.n-i)
    return downArray

# Alternative solution
class MyRange2:
  def __init__(self, n):
    self.n = n

  def __iter__(self):
    return self

  def next(self):
    myArray = []
    for i in range(self.n, -1, -1): # from n to 0
      myArray.append(i) # adds the even number to the list
    return myArray
  
myRange = MyRange2(8)
print(myRange.next())
