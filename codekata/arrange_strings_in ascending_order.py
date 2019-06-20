s=int(input())
x = [(x) for x in input().split()]
x = sorted(x, key=len)
for i in range(0,s-1):
    if(len(x[i])==len(x[i+1])): #arranging the words with same length lexicographically
        t=x[i]
        p=x[i+1]
        if(t[0]>p[0]):
            x[i+1]=t
            x[i]=p
        else:
            continue
print(*x,sep=' ')
