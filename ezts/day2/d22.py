class stack:
  def __init__(self):
    self.l=[]
  def push(self,data):
    self.l.append(data)
  def pop(self):
    self.l.pop()
  def peek(self):
    print(self.l[-1])
  def isEmpty(self):
    return len(self)==0
s=stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(2)
s.pop()
x=s.l
print(x)
#applications:cpmmand prompt backtrack
#queue also same with pop(0) change
for i in range(len(x)):
  a=x.pop()
  print(a)