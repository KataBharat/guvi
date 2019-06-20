x1,y1=input().split()
x1,y1=int(x1),int(y1)
x2,y2=input().split()
x2,y2=int(x2),int(y2)
x3,y3=input().split()
x3,y3=int(x3),int(y3)
#if ((y3 - y2)*(x2 - x1) == (y2 - y1)*(x3 - x2)):
if (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2):
    print ("yes") 
else: 
    print ("no")
