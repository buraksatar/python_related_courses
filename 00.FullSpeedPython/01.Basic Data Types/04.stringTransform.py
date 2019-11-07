def getStr(s):
  ## Write your code here
  ## Transform the string
  output_s = ''
  for each in s:
    output_s += each * 3
  ## Update length of string
  s = output_s
  strlen = len(s)
  return [s, strlen]