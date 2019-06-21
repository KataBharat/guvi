s=int(input())
for i in range(1,s):
    if(s%i==0):
        
        t=s/i
        if(t%2!=0):
            print(i)
            break
