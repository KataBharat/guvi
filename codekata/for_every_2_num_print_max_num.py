s=int(input())
x=[int(x) for x in input().split()]

for i in range(len(x)-1):
    if(x[i]>x[i]+1):
        print(x[i],end=' ')
    else:
        print(x[i+1],end=' ')
    
