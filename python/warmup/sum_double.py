'''
Given two int values, return their sum. 
Unless the two values are the same, then return double their sum.
'''

def sum_double(x,y):
  sum = x+y
  if x == y:
    return sum * 2
  return sum