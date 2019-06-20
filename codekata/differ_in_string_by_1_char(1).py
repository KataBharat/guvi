s11, s22 = input().split()
count1 = 0
for i in range(len(s11)):
  if s11[i]!=s22[i]:
    count1=count1+1
if count1==1:
  print ("yes")
else:
  print ("no")
