class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Linkedlist:
  def __init__(self):
    self.head=None
  def insertatbegin(self,d):
    new_node=Node(d)
    if self.head==None:
      self.head=new_node
      return
    else:
      new_node.next=self.head
      self.head=new_node
  def printlinkedlist(self):
    if self.head is None:
      print("LLS is empty")
      return
    itr=self.head
    while itr:
      print(itr.data,end='->')
      itr=itr.next
  def insertatend(self,v):
    newnode=Node(v)
    if not self.head:
      self.head=newnode
    else:
      itr=self.head
      while itr.next:
        itr=itr.next
      itr.next=newnode
  def deleteatend(self):
    if not self.head:
      return
    if self.head.next==None:
      self.head=None
    else:
      itr=self.head
      while itr.next.next!=None:
        itr=itr.next

      itr.next=None
  def countl(self,value):
    if not self.head:
      return
    count=0
    itr=self.head
    while itr:
      count+=1
      itr=itr.next
    print(count,":count and middle value is ",count//2)
    m=count//2
    i=0
    itr=self.head
    while i<m:
      itr=itr.next
      i+=1
    print(itr.data)
    newnode=Node(value)
    newnode.next=itr.next
    itr.next=newnode
  def search(self,v,d):
    if self.head is None:
      print("empty")
    else:
      newnode=Node(d)
      itr=self.head
      while itr:
        if itr.data==v:
          print("found")
          newnode.next=itr.next
          itr.next=newnode
          break
        itr=itr.next
      else:
        return "not found"
      
    
  '''def ifexists(self,d):
    if d<0 or d>:
      print("exists")
    else:
      print("no")'''

  """def deletefirst(self):
    if self.head is None:
      print("nothing to delete")
    else:
      self.head=self.head.next"""
 # def insertatindex(self,i):
    
  
    


x=Node(3)
x.next=Node(4)
x.next.next=Node(5)
x.next.next.next=Node(6)

y=Linkedlist()
#y.insertatbegin(5)
y.insertatbegin(6)
y.insertatbegin(8)
y.insertatbegin(9)
y.insertatbegin(2)
y.insertatbegin(3)
#y.deletefirst()
#y.deleteatend()
#y.countl(7)
#y.ifexists(3)
y.search(8,114)
print(y.printlinkedlist())