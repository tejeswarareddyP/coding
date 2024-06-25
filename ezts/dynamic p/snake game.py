
import random
def board(sl,pos,pos2):
  for i in range(10,0,-1):
    for j in range(1,11):
      #print(i,j)
      n=i*10-j
      if n==pos:
        print("[p1]",end=" ")
      if n==pos2:
        print("[p2]",end=" ")
      elif n in sl:
        print("[s]",end=" ")
      else:
        print("[ ]",end=" ")
    print()
def bussu(sl,pos):
  if pos in sl:
    pos=sl[pos]
    print("you have been bitten by snake")
    return pos
  elif pos in sl.values():
    for i in sl:
      if pos==sl[i]:
        print('you have stepped on a ladder')
        pos=i
        return pos
  else:
    return pos


pos=0
pos2=0
sl={95:5,80:20,46:21,38:26,57:25,65:15,70:18,62:9,73:24}
board(sl,pos,pos2)
def random1():
  return random.randint(1,6)
curr=pos
while pos<100 and pos2<100:
  if curr==pos:
    print("your player 1 is in",pos)
    print("your current position is",pos)
    input("press Enter to play")
    dice=random1()
    print("dice has gave",dice)
    pos+=dice
    print("_"*20)
    pos=bussu(sl,pos)  
    board(sl,pos,pos2)
    print("current pos",pos)
    curr=pos2
  else:
    print("your player 2 is in",pos2)
    print("your current position is",pos2)
    input("press Enter to play")
    dice=random1()
    print("dice has gave",dice)
    pos2+=dice
    print("_"*20)
    pos2=bussu(sl,pos2)  
    board(sl,pos,pos2)
    print("current pos",pos2)
    curr=pos

print("congo")

  

  
print("congratulations")

sl={95:5,6:13,9:90,46:8,18:4,19:2,99:1}













'''s={}
l={}
n=int(input("enter no. of snakes and ladders"))
for i in range(n):
  k=input("key:")
  v=input("value:")
  s[k]=v'''