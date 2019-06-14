# just change print staments in prime.py program

x=int(input())
n=x//2
t=0
for i in range(2,x):
  if(x%i==0):
    t=1
if(t==0):
  print("no")
if(t==1):
  print("yes")
