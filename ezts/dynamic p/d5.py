board=[["  "]*3 for i in range(3)]
for i in board:
    print("|".join(i))
    print("_"*10)
def issafe(a,b):
    if board[a][b]=="  ":
        return True
    else:
        return False
def win(b,cur,r,c):
    for i in range(3):
       if  b[r][0]==cur and b[r][1]==cur and b[r][2]==cur:
           return True
    for i in range(3):
        if  b[0][c]==cur and b[1][c]==cur and b[2][c]==cur:
           return True
    for i in range(3):
        if b[i][i]!=cur:
            break
    for i in range(3):
        if b[i][2-i]!=cur:
            break
    return False 
 
def isfull(board):
    for i in board:
        for j in i:
            if j=="  ":
                return False
    return True
 
def playtic(board):
 
  curr='x'
  while True:
    print("current player is",curr)
    print("enter row and col")
    a,b=list(map(int,input().split(" ")))
    if a>=0 and a<3 and b>=0 and b<3:
        if issafe(a,b):
            board[a][b]=curr
    for i in board:
        print("|".join(i))
    print("_"*10)
    if win(board,curr,a,b):
        print("congrats ,player",curr,"wins")
        break
    if isfull(board):
        print("draw")
        break
    if curr=="x":
        curr="0"
    else:
        curr="x"  
playtic(board)