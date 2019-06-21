s=int(input())
s=[int(x) for x in input().split()]
s1=sorted(s)
if(s==s1):
    print("yes")
else:
    print("no")
