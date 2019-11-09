class MyRange:
  def __init__(self, n):
    self.n = n

  def __iter__(self):
    return self

  def next(self):
    #write your code here
    n1=0
    n2=1
    fibonacci_array = [n1,n2]
    for i in range(self.n-2):
      result = n1 + n2
      n1 = n2
      n2 = result
      fibonacci_array.append(result)
    return fibonacci_array

# Better Solution
class MyRange2:
  def __init__(self, n):
    self.n = n

  def __iter__(self):
    return self

  def next(self):
    myArray = []
    for i in range(self.n): # from n to 0
      if i == 0 or i == 1:
        myArray.append(i) # adds the even number to the list
      else:
        myArray.append(myArray[i-2] + myArray[i-1])
    return myArray
  
myrange = MyRange2(8)
print(myrange.next())