# Implement the hasDuplicates function which verifies if a list has duplicate values.

def hasDuplicates(list):
  # write code here
  for i in range(len(list)):
    for j in range(len(list)):
      if (i!=j) and (list[i] ==list[j]):
        return True
  return 
  
# Better solution
def has_duplicates(list):
  flag = 0
  for i in range (len(list)):
    for j in range (i+1,len(list)):
        if (list[i] == list[j]):
          flag = 1
  if (flag == 1): 
     return True
  else:
     return False
  
l=[1, 2, 3, 4, 5]  
print(has_duplicates(l))
l=[1, 2, 3, 3, 4]  
print(has_duplicates(l))