import math
c=0
s=[int(x) for x in input().split()]
for i in range(s[0],s[1]+1):
    t=str(math.sqrt(i))
    print(t)
    if('.0' in t):
        c=c+1
print(c)
        
