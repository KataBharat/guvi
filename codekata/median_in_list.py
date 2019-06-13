n = int(input())
a = [int(x) for x in input().split()]
a.sort()
print(a[int(len(a)/2)])
