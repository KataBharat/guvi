a,b=map(int,input().split())
for i in range(a,b):
  temp=i
  sum1 = 0
  while(i!=0):
    r = i%10
    sum1 = sum1 + (r**3)
    i = i//10
  if(sum1==temp):
    print(temp,end=' ')
