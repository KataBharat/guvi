s1=int(input())
s2=[int(x) for x in input().split()]
for i in s2:
    if(i<s1):
      print(i,end=' ')
