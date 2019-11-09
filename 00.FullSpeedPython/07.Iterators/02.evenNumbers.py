class MyRange:
  def __init__(self, n):
    self.n = n

  def __iter__(self):
    return self

  def next(self):
    evenArray = []
    for i in range(1, self.n+1):
      if i % 2 is 0:
        value = i
        evenArray.append(i)
      else:
        i+=1
    return evenArray
    
myrange = MyRange(8)
print (myrange.next())