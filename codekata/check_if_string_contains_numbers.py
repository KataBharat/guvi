s=input()
t=0
for i in s:
    if(i.isalpha()):
        t=1
        break
if(t==1):
    print("no")
else:
    print("yes")
