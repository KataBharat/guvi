s=[int(x) for x in input().split()]
t=0
if 0 not in s and sum(s)==180:
    print("yes")
else:
    print("no")
