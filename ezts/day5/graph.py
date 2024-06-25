"""class graph:
  def __init__(self):
    self.g={}
  def addedge(self,a,b):
    if a not in self.g:
        self.g[a]=[]
        self.g[a].append(b)
    else:
      self.g[a].append(b)      
  def printlist(self):
        print(self.g)
"""
'''
class graph:
  def __init__(self):
    self.d={}  
  def printlist(self):
        print(self.d)
  def addedge(self,a,b):
     if a not in self.d:
        self.d[a]=[]
        self.d[a].append(b)
     else:
        self.d[a].append(b)



  def bfs(self,root):
    queue=[root]
    visited=[root]
    while queue:
      curr=queue.pop(0)#for dfs pop()
      print(curr) 
      if curr in self.d:
        for i in self.d[curr]:
          if i not in visited:
            visited.append(i)
            queue.append(i)

'''
map=[[1,1,0,0,1],
     [1,1,0,0,1],
     [0,0,1,0,0],
     [0,0,1,0,1]]
c=0
def helper(map,i,j):
  if i<0 or j<0 or i>4 or j>4:
    return
  elif map[i][j]==0:
    helper(map,i-1,j)
    helper(map,i+1,j)
    helper(map,i,j-1)
    helper(map,i,j+1)
for i in range(len(map)-1):
  for j in range(len(map)-1):
    if map[i][j]==1:
      c+=1
      
print(c)





t=graph()
t.addedge(1,2)
t.addedge(1,4)
t.addedge(2,1)
t.addedge(3,1)
t.addedge(4,1)
t.addedge(3,1)
t.addedge(2,1)
t.addedge(2,1)
t.addedge(2,1)
t.addedge(2,1)
t.addedge(2,1)
t.addedge(2,1)
t.printlist()
