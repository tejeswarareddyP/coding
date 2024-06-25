a=[3,5,7,11,5,8]
b=[5,7,11,10,5,8]

from collections import Counter
def p(A,B):
  a=Counter(A)
  b=Counter(B)
  c=0
  for i in a:
    if i in b:
      c+=min(a[i],b[i])
  if c==len(A):
    return c-1
  else:
    return c+1
print(p(a,b))