s1=int(input())
x=[int(x) for x in input().split()]
x=sorted(x)
print(x[s1-1]-x[0])
