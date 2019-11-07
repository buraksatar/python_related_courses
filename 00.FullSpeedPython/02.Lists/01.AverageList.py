def getAverage():
  l1 = [1, 4, 9, 10, 23]
  ## Write your code here
  sum_list = 0
  for each in l1:
    sum_list += each

  avg = sum_list/len(l1) ## Calculate the average here
  return avg