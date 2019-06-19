s=int(input())
l=[]
for i in range(0,s):
    
    l.append(input())
c=0
s1=['a','a','b','i','k','l']
for i in l:
    i=sorted(i)
    if(i==s1):
        c=c+1
print(c)
