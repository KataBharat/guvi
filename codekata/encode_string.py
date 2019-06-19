s=input()
s2=''
s1='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
for i in s:
    if i in s1:
        t=s1.index(i)
        t=t+3
        s2=s2+s1[t]
print(s2)
