l=[8,9,10]
def partition(l,beg,end):
   while True:
      start=beg
      stop=end
      pi=l[beg]
      while start<len(l) and l[start]<pi:
         start+=1
      while stop>-1 and l[stop]>pi:
         stop-=1
      if start<stop:
         l[start],l[stop]=l[stop],l[start]
      return stop
def quick(l,i,j):
   if i<j:
      p=partition(l,i,j)
      quick
  