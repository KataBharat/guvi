x=[x for x in input().split()]
x[2]=int(x[2])
count1 = 0
for i in range(len(x[0])):
    t=x[0]
    p=x[1]
    if t[i]!=p[i]:
        count1=count1+1
if count1==x[2]:
  print ("yes")
else:
  print ("no")
