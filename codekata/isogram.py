s= input()
s = s.lower() 
s2=""
for i in s:
  if i not in s2:
      s2=s2+i
if(s==s2):
  print("Yes")
else:
  print("No")
 
