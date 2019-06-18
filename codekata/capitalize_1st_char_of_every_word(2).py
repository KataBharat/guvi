x=input()
print(' '.join(s[:1].upper() + s[1:] for s in x.split(' ')))
