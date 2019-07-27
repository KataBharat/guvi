x=int(input())
s=[int(x) for x in input().split()]
s=sorted(s)
k=''
sum1=0
for i in range(len(s)-1,-1,-1):
        sum1=sum1+i
        k=k+str(s[i])
if(sum1>0):
    print(k)
else:
    print("0")
