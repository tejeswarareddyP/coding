class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None

class Trees:
  def __init__(self):
    self.root=None
  def insert(self,value):
    newnode=Node(value)
    if not self.root:
        self.root=newnode
    else:
      curr=self.root
      while True:
        if curr.data>value:
          if curr.left==None:
            curr.left=newnode
            break
          else:
            curr=curr.left
        else:
          if curr.data>value:
           if curr.right==None:
            curr.right=newnode
            break
           else:
             curr=curr.right
  def preoder(self):
    self.helper(self.root)
  def helper(self,root):
    if root:
      print(root.data)
      self.helper(root.left)
      self.helper(root.right)
t=Trees()
t.insert(9)
t.insert(7)
t.insert(1)
t.insert(5)
t.insert(2)
t.insert(4)
t.preoder()




    