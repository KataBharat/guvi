x=[int(x) for x in input().split()]
y=[int(x) for x in input().split()]
for i in y:
    c=0
    if(y.count(i)==x[1]):
        print(i)
        break
    
