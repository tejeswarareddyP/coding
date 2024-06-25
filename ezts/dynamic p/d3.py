#fib memoization
g=0

def fib(n,memo={}):
  global g
  g+=1
  if n<2:
    return n
  if n in memo:
    return memo[n]
  else:
    memo[n]= fib(n-1)+fib(n-2)
    return memo[n]

#print(fib(10))
#print(g)
#fib tabulation
def f(n,memo={}):
  global c
  memo=[0]*(n+1)
  memo[1]=1
  for i in range(2,n+1):
    c+=1
    memo[i]=memo[i-1]+memo[i-2]
  return memo[n]
c=0
print(f(10))
print(c)

