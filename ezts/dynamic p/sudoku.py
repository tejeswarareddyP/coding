grid =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
def empty(grid):
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j]==0:
        return (i,j)
  return None
def isvalid(grid,r,c,no):
  for i in range(9):
    if grid[r][i]==no:
      return
  for i in range(9):
    if grid[i][c]==no:
      return
   


  nrow=3*(r//3)
  ncol=3*(c//3)
  for i in range(nrow,nrow+3):
    for j in range(ncol,ncol+3):


def sudoku(gird):
  emptyccell=empty(gird)
  if emptyccell is None:
    for i in grid:
      print(i)
    return
  r,c=emptyccell
  for i in range(1,9):
    if isvalid(grid,r,c,i):
      grid[r][c]=i
      if soduko(gird):
        return True
      grid[r][c]=0
  return False
sudoku(grid)

  
