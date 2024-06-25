n=12221
n1=12221
rev=0
while n>0:
  r=n%10
  rev=rev*10+r
  n//=10
print(rev)

if rev==n1:
  print("palin")
else:
  print("no")