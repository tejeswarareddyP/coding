#prime
n=8
for i in range(2,int(n**(1/2))):
  if n%i==0:
    print("not prime")
    break
else:
  print("prime")

