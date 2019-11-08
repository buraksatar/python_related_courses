def isSorted(list):
  # write your code here
  for index in range(len(list)-1):
    if list[index] > list[index+1]:
      return False
  return True

# Alternative Solution
def isSorted(list):
  flag = 0
  i = 1
  while i < len(list): 
      if(list[i] < list[i - 1]): # compare with the previous element
          flag = 1
      i += 1
      
  if (not flag) : 
      return True 
  else : 
      return False 
print(isSorted([1,2,3,4,5]))
print(isSorted([1,2,5,4,2]))