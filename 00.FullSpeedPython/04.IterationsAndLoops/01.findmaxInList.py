def findMaximumValueIndex(list):
  # write your code here
  max_index = 0
  max_num = list[0]
  for index, each in enumerate(list):
    if each > max_num:
      max_num = each
      max_index = index
  return [max_index, max_num]
  # return [index,maximum] #return your index and maximum in the form of a list