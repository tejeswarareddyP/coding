map=[['0','-','-','0','-'],
     ['0','0','s','0','-'],
     ['-','-','-','0','-'],
     ['-','0','-','-','e']]
word="-"
def check(map,i,j,path,c):
  
  if [i,j] in path:
    return False
  if i<0 or i>=len(map) or j<0 or j>=len(map[0]):
      return False
  if map[i][j]=='e':
    print(path)
    return True
  if map[i][j]=="0":
    
    return False
  path.append([i,j])
  a=check(map,i-1,j,path,c+1) or check(map,i+1,j,path,c+1) or check(map,i,j-1,path,c+1) or check(map,i,j+1,path,c+1)
  path.pop()
  return a
c=1
r=len(map)
co=len(map[0])
path=[]
for i in range(r):
  for j in range(co):
    if map[i][j]=="s":
      if check(map,i,j,path,c):
        print("congrats")
        exit()

else:
  print("Not no congrats")

