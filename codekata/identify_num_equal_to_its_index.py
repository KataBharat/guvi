x=int(input())
s=[int(x) for x in input().split()]
k=[]
for i in range(len(s)):
    if(i==s[i]):
        k.append(s[i])
if(len(k)>0):
    print(*(sorted(k)),end=' ')
else:
    print('-1')
