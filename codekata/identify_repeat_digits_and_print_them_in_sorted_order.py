s=[int(x) for x in input().split()]
l=[]
k=[]
for i in s:
    if i not in l:
        l.append(i)
for i in l:
    t=0
    for j in s:
        if(i==j):
            t=t+1
    if(t>1):
        k.append(i)
        
print(*(sorted(k)),end='')
