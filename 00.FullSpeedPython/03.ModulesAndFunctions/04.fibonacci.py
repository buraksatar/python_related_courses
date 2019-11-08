def fibonacci(n):
   ## write base case
   if n == 0:
      return 0
   elif n == 1:
      return 1
   ## write recursive case 
   return fibonacci(n-1)+fibonacci(n-2)

# alternative solution
def fibonacci2(n):
  if n <= 1:
       return n
  else:
       return(fibonacci(n-1) + fibonacci(n-2))
print(fibonacci2(4))    
    