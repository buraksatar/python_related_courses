# section 1

def getSquare():
  ## Write your code here
  l1 = [ x*x for x in range(1,11)] ## Create your list here
  return l1

# section 2

def ListofEvenOdds1():
  l1 = [x for x in range(0,21) if x%2==0] # list of even numbers
  l2 = [x for x in range(0,21) if x%2==1] # list of odd numbers 
  return [l1, l2]

def ListofEvenOdds2():
  l1 = []
  l2 = []  
  l1 = [x for x in range(0, 21) if (x % 2 == 0)]
  l2 = [x for x in range(0, 21) if (x not in l1)]
  return[l1, l2]
  
print(ListofEvenOdds2())

# section 3

def evenSquareSum():
  even = [x * x for x in range(0, 21, 2)]
  return sum(even)
  
print(evenSquareSum())

# section 4 
def getSquare2():
  """
  Given a getSquare() function, 
  make a list comprehension that 
  returns a list with the squares of 
  all even numbers from 0 to 20, 
  but ignores those numbers that are divisible by 3
  """
  l1 = [x**2 for x in range(0,21) if (x%2==0) and (x%3!=0)] ##Create the list here
  return l1