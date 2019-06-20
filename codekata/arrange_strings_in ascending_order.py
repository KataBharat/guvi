s=int(input())
x = [(x) for x in input().split()]
x=sorted(x,key=len)
for i in range(len(x)-1):
    if len(x[i])==len(x[i+1]) and x[i]>x[i+1]:
        x[i],x[i+1]=x[i+1],x[i]
print(*x)
