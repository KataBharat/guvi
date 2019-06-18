x1,x2=input().split()
x1,x2=int(x1),int(x2)
count=0
for i in range(x1,x2+1):
  n=i//2
  t=0
  for j in range(2,n+1):
    if(i%j==0):
      t=1
  if(t==0):
    count+=1
print(count)
