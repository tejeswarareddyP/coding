map=[['t','b','h','s','a'],
     ['c','n','c','j','a'],
     ['a','e','t','e','j'],
     ['p','a','d','p','a']]
word="teja"
c=0
def check(map,i,j,k,path):
  if k==len(word):
    print(path)
    return True
  if [i,j] in path:
    return False
  if i<0 or i>=len(map) or j<0 or j>=len(map[0]):
      return False
  if word[k]!=map[i][j]:
    return False
  path.append([i,j])
  return check(map,i-1,j,k+1,path) or check(map,i+1,j,k+1,path) or check(map,i,j-1,k+1,path) or check(map,i,j+1,k+1,path)
r=len(map)
co=len(map[0])
path=[]
for i in range(r):
  for j in range(co):
    if map[i][j]==word[0]:
      if check(map,i,j,0,path):
        print("Exists")
        exit()

else:
  print("Not exists")