#Linear Search
l=[1,2,3,4,5,6,7,8,9]
k=6
i=0
j=len(l)-1
while i<j:
  mid=(i+j)//2
  if l[mid]==k:
    print(mid)
    break
  elif l[mid]<k:
    i=mid+1
  else:
    j=mid-1
else:
  print("not found")


