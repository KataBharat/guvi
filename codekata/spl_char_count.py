n=input()
c=0
for i in range(len(n)):
  if(n[i].isdigit() or n[i].isalpha() or n[i]==' '):
    continue
  else:
    c+=1
print(c)
