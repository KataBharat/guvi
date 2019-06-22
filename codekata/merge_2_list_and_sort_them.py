s1,s2=input().split()
s1=int(s1)
s2=int(s2)
x=[int(x) for x in input().split()]
y=[int(x) for x in input().split()]
z=x+y
print(*(sorted(z)),end=' ')
