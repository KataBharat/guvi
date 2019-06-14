s=int(input())
t=0
a = [int(x) for x in input().split()]
for i in range(a[o]-1,a[1]):
  if (i==s):
    t=1;
if(t==1):
  print("yes")
else:
  print("no")
