import sys
def f(n):
  if n==5:
    return 1
  
  print(n)
  return f(n+1)

  

f(1)