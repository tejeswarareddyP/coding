def reverse(n,rev):
  if n==0:
    return rev
  rem=n%10
  rev=rev*10+rem
  return reverse(n//10,rev)

print(reverse(1234,0))