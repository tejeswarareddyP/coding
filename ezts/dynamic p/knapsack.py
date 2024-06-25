

def knapsack(v,w,n,c):
  if n==0 or c==0:
    return 0
  if w[n-1]>c:
    knapsack(v,w,n-1,c)
  else:
    return max(v[n-1]+knapsack(v,w,n-1,c-w[n-1]),knapsack(v,w,n-1,c))


v=[100,200,300]
w=[10,20,30]
c=50
n=len(w)
print(knapsack(v,w,n,c))



