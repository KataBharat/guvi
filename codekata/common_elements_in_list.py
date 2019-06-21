x=int(input())
s1=[int(x) for x in input().split()]
s2=[int(x) for x in input().split()]
for i in s1:
  if(i in s2):
    print(i,end=' ')
