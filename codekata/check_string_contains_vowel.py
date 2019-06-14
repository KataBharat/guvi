s=input()
t=0
a=['a','e','i','o','u']
for i in s:
  if i in a:
    t=1
if(t==1):
  print("yes")
else:
  print("no")
