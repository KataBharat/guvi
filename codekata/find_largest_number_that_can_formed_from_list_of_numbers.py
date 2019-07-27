x=int(input())
s=[int(x) for x in input().split()]
s=sorted(s)
k=''
for i in range(len(s)-1,-1,-1):
    if(s[i]!=0):
        k=k+str(s[i])
if(len(k)>0):
    print(k)
else:
    print("0")
