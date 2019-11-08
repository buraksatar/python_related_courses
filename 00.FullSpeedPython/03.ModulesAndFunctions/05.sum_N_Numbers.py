# The sum of all numbers from 1 upto 
# that input natural number n

def sum_N_Numbers (n):
  if n == 1:
    return 1
  # Write code here
  return n + sum_N_Numbers(n-1)