s1=[int(x) for x in input().split()]
s2=[int(x) for x in input().split()]
s3=[]
for i in s2:
    if(i<s1[1]):
        s3.append(i)
print(*sorted(s3))
