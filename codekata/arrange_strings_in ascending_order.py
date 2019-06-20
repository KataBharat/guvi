s=int(input())
x = [(x) for x in input().split()]
x = sorted(x, key=len)
for i in range(0,s-1):
    if(len(x[i])==len(x[i+1])):
        t=x[i]
        p=x[i+1]
        for i in range(0,len(t)): #arranging strings of same length lexicographly
            if(t[i]>p[i]):
                x[i+1]=t
                x[i]=p
                continue
            else:
                continue
print(*x,sep=' ')
