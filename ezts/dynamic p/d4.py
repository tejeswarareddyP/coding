import random
a=1000
#random.randint(1,1000)
n=0
c=0
while n!=a:
  c+=1
  n=random.randint(1,1000)
  if n>a:
    n=random.randint(1,n)
else:
   n=random.randint(n,a)
print('congrats','number found is',n,c)