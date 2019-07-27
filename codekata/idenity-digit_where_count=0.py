x=int(input())
s=[int(x) for x in input().split()]
for i in s:
    if(s.count(i)==1):
        print(i)
        break
