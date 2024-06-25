def issafe(b,row,col,n):
  for c in range(col):
    if b[row][col]==1:
      return False
  while row<=0 and col<=0:
    if b[row][col]==1:
      return False
    row-=1
    col-=1
  while r>=0 and c<n:
    if b[r][c]==1:
      return False
    r-=1
    c+=1
    return True







def queen(b,r,n):
  if r==n:
    for i in b:
      print(i)
    print("*"*30)
    return
  for i in range(n):
    if issafe(b,r,i,n):
      b[r][i]=1
      if queen(b,r+1,n):
        print("true")
      b[r][i]=0


n=4
b=[[0]*n for i in range(n)]
queen(b,0,n)













n=4
b=[[0]*n for i in range(n)]
queen(b,0,0,n)

