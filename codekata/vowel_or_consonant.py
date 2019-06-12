c = input()

v = ['a','e','i','o','u']
con = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']

if(c in v):
    print("Vowel")
if(c in con):
    print("Consonant")
if(c not in v and c not in con):
    print("invalid")
