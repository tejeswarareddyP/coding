l=[1,4,6,7,3,9]
print(l)
for i in range(1,len(l)):
  m=l[i]
  j=i-1
  while j>-1 and m<l[j]:
    l[j+1]=l[j]
    j-=1
  l[j+1]=m
print(l)