x1=int(input())
n=x1//2
t=0
for i in range(2,x1):
  if(x1%i==0):
    t=1
if(t==0):
  print("yes")
if(t==1):
  print("no")
