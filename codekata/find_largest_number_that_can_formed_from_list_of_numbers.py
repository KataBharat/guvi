x=int(input())
s=[int(x) for x in input().split()]
s=sorted(s)
k=''
for i in range(len(s)-1,-1,-1):
    k=k+str(s[i])
print(k)
