import re
s=input()
if((bool(re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', s)))):
  print("Yes")
else:
  print("No")
