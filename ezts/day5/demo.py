'''def f(n):
  if n==1:
    return 1
  return n*f(n-1)

print(f(5))'''
def f1(n):
  s=0
  i=1
  for i in range(n):
    s=s+i
  return s
print(f1(5))