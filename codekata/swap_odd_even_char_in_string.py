s = list(input())
s1=''
for i in range(0,len(s),2):
  t=s[i]
  s[i]=s[i+1]
  s[i+1]=t
  s1=s1+s[i]+s[i+1]
print(s1)

