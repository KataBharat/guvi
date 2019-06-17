x=input()
print(' '.join(s[:1].upper() + s[1:] for s in x.split(' ')))

# other method
# print(x.title()) using title method
