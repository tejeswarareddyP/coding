map=[[1,1,0,0,1],
     [1,1,0,0,1],
     [0,0,1,0,0],
     [0,0,0,0,1]]

c=0
def check(map,i,j):
  if i<0 or i>=len(map) or j<0 or j>=len(map[0]):
      return
  if map[i][j]==0:
    return
  map[i][j]=0
  check(map,i+1,j)
  check(map,i-1,j)
  check(map,i,j-1)
  check(map,i,j+1)
r=len(map)
co=len(map[0])
for i in range(r):
  for j in range(co):
    if map[i][j]==1:
      c+=1
      check(map,i,j)

print(c)