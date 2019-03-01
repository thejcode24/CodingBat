'''
Given a non-empty string like "Code" return a string like "CCoCodCode".
'''


def string_splosion(str):
  
  for i in range(len(str)):
    if len(str) == 1:
      return(str[0])

    else:
      print(str[0:i+1], end="")
    