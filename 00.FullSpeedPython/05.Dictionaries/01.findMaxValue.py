def oldestStudent(ages):
  max = 0
  key = 0
  for key, value in ages.items():
    if value > max:
      max = value
      key = key
  #write code here
  return key

# Alternative Solution
def oldestStudent(ages):
  
  value = list(ages.values())
  key = list(ages.keys())
  return key[value.index(max(value))]

ages = {
     "Peter": 10,
     "Isabel": 11,
     "Anna": 9,
     "Thomas": 10,
     "Bob": 10,
     "Joseph": 11,
     "Maria": 12,
     "Gabriel": 10,
  }
print(oldestStudent(ages))