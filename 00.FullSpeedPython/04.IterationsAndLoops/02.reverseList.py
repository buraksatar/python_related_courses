def reverse(list):
  # Write your code here
  new_list = []
  for index, each in enumerate(list):
    new_list.append(list[len(list)-1-index])
  return new_list
  # return new_list # uncomment this line when you write code

  # Alternative Solution
  def reverse(list):
    length = len(list)
    s = length

    new_list = [None]*length

    for item in list:
        s = s - 1
        new_list[s] = item
    return new_list
    
list=[1, 2, 3, 4, 5]
print(reverse(list))