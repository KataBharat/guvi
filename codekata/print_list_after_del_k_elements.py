x=[int(x) for x in input().split()]
y=[int(x) for x in input().split()]
print(*y[:-x[1]],end=' ')
