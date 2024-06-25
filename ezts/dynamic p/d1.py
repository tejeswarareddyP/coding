'''def p(n,i=2):
    if n==0 or n==1:
      return 0
    if n%i==0 or n%n-1==0:
      return 0
    return p(n,i+1)

i=2    
n=100
for a in range(2,n-1):
    if (p(a)):
       print(a)
'''
def fun(i,n):          
    if i==n-1:           
        if n%n-1==0:
            return 1
        else:
            return None
    else:
        if n%i==0:
            return 1
        return fun(i+1,n)
def main(i,n):             
    if i==n:
        k=fun(2,i)
        if k==1:
            print(i,"not prime")
        else:
            print(i,"prime")
    else:
        k=fun(2,i)
        if k==1:
            print(i,"not prime")
        else:
            print(i,"prime")
        main(i+1,n)
main(3,10)