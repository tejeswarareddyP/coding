l=[1,2,3,4,5,6]
m=l[0]
for i in l:
  if i>m:
    m=i
print(m)
s=min(l)
for i in l:
  if i>m & i!=m:
    s=i
print(s)
#smallest and second smallest
l=[1,2,3,4,5,6]
n=len(l)
m1=l[n-1]
for i in l:
  if i<m1:
    m1=i
print(m1)
s1=max(l)
for i in l:
  if i<m1 & i!=m1:
    s1=i
print(s1)