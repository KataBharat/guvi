s11, s22 = input().split()
count = 0
for i in range(len(s11)):
  if s11[i]!=s22[i]:
    count=count+1
if count==1:
  print ("yes")
else:
  print ("no")
