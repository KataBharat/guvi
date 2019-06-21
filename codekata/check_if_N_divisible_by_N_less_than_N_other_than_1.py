s=int(input())
t=0
for i in range(s-1,2,-1):
    if(s%i==0):
        t=1
        break
if(t==1):
    print("yes")
else:
    print("no")
