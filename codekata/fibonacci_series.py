n1=int(input())
a = 0
b = 1
for i in range(0,n1):
  print(b,end = " ")
  c = a + b
  a = b
  b = c
