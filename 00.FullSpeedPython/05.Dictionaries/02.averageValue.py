def calculateAverageAge(students):
  # Write code here
  sum = 0
  for key in students:
    sum += students[key]['age']

  return sum/len(students)   

  # Alternative Solution
  def calculateAverageAge(students):
  result = {}
  add_age = 0
  for thing in students.values():
      age = thing['age']
      add_age = add_age + age
    
  return(add_age / len(students.keys()))

students = {
      "Peter": {"age": 10, "address": "Lisbon"},
      "Isabel": {"age": 11, "address": "Sesimbra"},
      "Anna": {"age": 9, "address": "Lisbon"},
      "Gibrael": {"age": 10, "address": "Sesimbra"},
      "Susan": {"age": 11, "address": "Lisbon"},
      "Charles": {"age": 9, "address": "Sesimbra"},
  }
print(calculateAverageAge(students))