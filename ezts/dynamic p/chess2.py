n=8
b=[[-1]*n for i in range(n)]
#
# 
# print(b)
km=[(-1,-2),(-2,-1),(1,-2),(-2,1),(1,2),(2,1),(-1,2),(2,-1)]
def issafe(r,c,b,n):
  return (0<=r<n and 0<=c<n and b[r][c]==-1)

def kn(b,r,c,n,m):
  if m==n*n:
    for i in b:
      print(i)
      print(b)
    return True
  for j in km:
    newrow=r+j[0]
    newcol=c+j[1]
    if issafe(newrow,newcol,b,n):
      b[newrow][newcol]=m
      if kn(b,newrow,newcol,n,m+1):
        return True
      b[newrow][newcol]=-1
  return False


b[0][0]=0

kn(b,0,0,n,1)

    
   
  
















