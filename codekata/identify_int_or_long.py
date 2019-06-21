n1 = int(input())
if n1 >= -32767 and n1 <= 32767:
  print("INT")
elif n1 >= -2147483647 and n1 <= 2147483647:
  print("LONG")
elif n1 >= -9223372036854775807 and n1 <= 9223372036854775807:
  print("LONG LONG")
