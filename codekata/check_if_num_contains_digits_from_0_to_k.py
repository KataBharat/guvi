a,b = input().split()
b=int(b)
t=0
for i in range(b+1):
  if(str(i) in a):
    t=t+1
if(t==b):
  print("yes")
else:
  print("no")
