a = int(input())
b = [int(x) for x in input().split()]
for i in range(len(b)-1):
  if(b[i]>b[i+1]):
    print(i)
