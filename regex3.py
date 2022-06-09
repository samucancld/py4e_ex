# ^  = startswith
# .  = anything
# *  = 0 o más veces
# \S = non-whitespace char
# +  = 1 or + times
# [] = inside is what we want 4 a single char
#    = greedy; match the wider match
# ?  = non-greedy
# () = beginning and ending of the extraction
# [^ ] = everything BUT a space (in this case)

import re

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x) #match todo lo que sean numeros en x
print(y)

v = 'boca river racing boca a veces boca gana pero boca siempre es boca'
w = re.findall('[boca]+',v)
print(w)

a = 'From: Using the : character'
b = re.findall('^F.+?:',a)
print(b)

c = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
d = re.findall('\S+@\S+',c)
print(d)

e = re.findall('^From (\S+@\S+)',c)
print(e)

f = re.findall('@([^ ]*)',c)
g = re.findall('@([\S]*)',c)
h = re.findall('^From .*@([^ ]*)',c)
print(f,g,h)
