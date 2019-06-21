s=int(input())

for z in range(2,s+1):
  if(s%z==0) and (z%2==0):
      print(z,end=' ')
