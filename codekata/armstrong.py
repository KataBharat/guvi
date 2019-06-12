x = int(input())
temp=x
sum1 = 0
while(x!=0):
  r = x%10
  sum1 = sum1 + (r**3)
  x = x//10
if(sum1==temp):
  print("yes")
else:
  print("no")
