import math
n, k = input().split()
n=int(n)
k=int(k)
print(int(math.factorial(n)/math.factorial(n-k)))
