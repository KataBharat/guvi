s=int(input())
x=[int(x) for x in input().split()]
c=0
for i in range(s):
    for j in range(s):
        if(x[i]<x[j]):
            c=c+1
print(c)
