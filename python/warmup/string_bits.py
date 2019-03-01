'''
Given a string, return a new string made of every other char starting with the first
'''

def string_bits(string):

  r = ""
  for i in range(len(string)):
    if i % 2 == 0:
      r+=string[i]
  return(r)
 