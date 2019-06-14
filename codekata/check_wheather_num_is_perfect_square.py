import math
a = [int(x) for x in input().split()]
if('.0' not in str(math.sqrt(a[0]*a[1]))):
  print("no")
else:
  print("yes")
