a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
t=0
for i in b:
  if((i%2!=0) and (t==a[1])):
    print(i)
    t=t+1
  else:
    t=t+1
