def odd(n):
  # write your code here
  for each in range(1,n+1):
    if each % 2 == 1:
      yield each
  