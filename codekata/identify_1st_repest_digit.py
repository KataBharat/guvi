x=int(input())
s=[int(x) for x in input().split()]
k=0
for i in s:
    if(s.count(i)>1):
        print(i)
        k=k+1
        break
if(k==0):
    print("unique")
    
