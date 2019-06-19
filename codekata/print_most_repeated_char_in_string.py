s = input()
c = []
for i in range(len(s)):
  c.append(s.count(s[i]))
i = c.index(max(c))
print (s[i])

#explanation
# consider string - aabbbc
# c list will be 2,2,3,3,3,1
# max of c will return 3
# index of 3 will give the 1st index of 3 in c list # # that is 2
# finally s[2] will be printed as the most repeated   #  character 
