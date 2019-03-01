'''
Given a string, return a new string where "not " has been added to the front. 
However, if the string already begins with "not", return the string unchanged. 
'''

def not_string(s):
  r = s.split(" ")
#   if r[0]=="not":
#     return s
#   else:
#     return "not "+s 

  return(s if r[0]=="not" else "not "+s)