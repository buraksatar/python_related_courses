def findOccurence(s):
  # Write your code here
  #a = 0#find first occurrence of "b" in the string 
  #b = 0#find first occurence  of "ccc" in the string
  a = s.index('b')
  b = s.index('ccc')
  return [a, b]

  # Alternative Solution
  def findOccurence(s):
  a = s.find("b")#find first occurrence of "b" in the string 
  b = s.find("ccc")#find first occurence  of "ccc" in the string
  return [a, b]

str = "aaabbccc"
print(findOccurence(str))