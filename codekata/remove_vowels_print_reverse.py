s=int(input())
s1=input()
t=0
s2=['a','e','i','o','u']
for i in s1:
  if(i in s2):
    s1 = s1.replace(i,"")
print(s1[::-1])
