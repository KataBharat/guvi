a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
t=0
for i in b:
  if (i==a[1]):
    t=1
if(t==1):
  print("yes")
else:
  print("no")
