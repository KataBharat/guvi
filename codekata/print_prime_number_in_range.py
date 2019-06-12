a,b=map(int,input().split())

for i in range(a,b):
  x=i//2
  t=0
  for y in range(x):
    if(i%x==0):
      t=1
  if(t==0):
    print(i,end=' ')
