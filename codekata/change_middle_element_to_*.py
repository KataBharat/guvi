n1=list(input())
if len(n1)%2==0:
    n1[int(len(n1)/2)] ='*'
    n1[int(len(n1)/2)-1]='*'
else:
    n1[int(len(n1)/2)] ='*'
for i in range(0,len(n1)):
    print(n1[i],end='')
