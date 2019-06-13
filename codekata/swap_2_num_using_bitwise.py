a = [int(x) for x in input().split()]
x=a[0];
y=a[1];
x = x ^ y; 
y = x ^ y; 
x = x ^ y;
print(x,y)
