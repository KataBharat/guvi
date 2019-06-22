s=int(input())
x=[int(x) for x in input().split()]
for i in range(s-1):
    if(x[i]>x[i+1]):
        print(i+1)
        break
