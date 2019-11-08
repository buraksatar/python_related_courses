def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n * factorial(n-1))
print("Factorial:")
print(factorial(5))