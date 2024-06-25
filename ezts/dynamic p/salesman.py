map=[[0,10,25,14],
     [10,0,16,15],               
     [25,16,0,20],
     [14,15,20,0]]
n=len(map)                  #n=4
def tsp(v,pos):
  if len(v)==n:              #
    return map[pos][0]      #
  m=float('inf')
  for i in range(n):
    if i not in v:
      nev=v+[i]
      ned=map[pos][i]+tsp(nev,i)
      m=min(m,ned)
  return m
v=[0]
ini=0
print(tsp(v,ini))
