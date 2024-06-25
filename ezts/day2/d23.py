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



s='5678+-*'
ls=stack()
ls.push(s if s.isdigit())
x=ls.l
for i in s:
  if i.isdigit():
    ls.push(int(i))
  elif i=='+':
    a=x.pop()
    b=x.pop()
    x.append(a+b)
  elif i=='-':
    a=ls.pop()
    b=ls.pop()
    x.append(a-b)
  elif i=='*':
    a=ls.pop()
    b=ls.pop()
    x.append(a*b)
  else:
    print("empty")

print(x)
