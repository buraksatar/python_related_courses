def fibonacci(n):
  myArray = []
  for i in range(n):
    if i is 0 or i is 1:
      myArray.append(i)
      yield i
    else:
      x = myArray[i-2] + myArray[i-1]
      myArray.append(x)
      yield x
      
for i in fibonacci(8):
  print(i)