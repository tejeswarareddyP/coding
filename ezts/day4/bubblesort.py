l=[1,2,3,7,6,5,4]
i=0
j=0
for i in range(len(l)-1):
  for j in range(len(l)-i-1):
    if l[j]>l[j+1]:
      l[j],l[j+1]=l[j+1],l[j]
print(l)
